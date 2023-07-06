from bs4 import BeautifulSoup
import requests
import pandas as pd
import glob
import os
import datetime
from settings import *
from unidecode import unidecode


class WebScraper:
    def __init__(self, url):
        self.url = url

    def scrape_website(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')

            content_core = soup.find('div', {"id": "content-core"})
            paragraphs = content_core.find(
                "div", {"id": "parent-fieldname-text"})
            all_ul = paragraphs.find_all("ul")

            count = 0
            for ul in all_ul:
                anchors = ul.find_all("a", href=True)

                for anchor in anchors:
                    link = anchor['href']
                    filename = link.split("/")[-1]

                    response = requests.get(link)
                    data = response.content

                    with open(filename, "wb") as f:
                        f.write(data)

                    print(
                        filename, " Baixado com Sucesso.")

                    count += 1
                    if count == 2:
                        break

                if count == 2:
                    break
        except requests.exceptions.RequestException as e:
            print("Erro durante o scraping:", e)


class FormatSheet:
    def __init__(self):

        self.directory = caminho_formatado
        self.archive = "revendas_lpc_*.xlsx"
        self.archive_trash = "resumo_semanal_lpc_*.xlsx"

    def find_file(self):
        try:
            archive_path = os.path.join(self.directory, self.archive)
            archive_trash_path = os.path.join(
                self.directory, self.archive_trash)

            self.archive_files = glob.glob(archive_path)
            self.archive_trash_files = glob.glob(archive_trash_path)
            print("Mapeando os arquivos......")
            return self.archive_files[0]
        except TypeError:
            return ("Erro ao achar o arquivo")

    def exclude_undesired(self):
        try:
            formatsheet = FormatSheet()
            if formatsheet:
                desired_file = self.archive_files[0]
                undesired_file = self.archive_trash_files[0] if self.archive_trash_files else None

                if undesired_file:
                    os.remove(undesired_file)
                    os.remove(desired_file)
                    print("Excluindo os arquivos baixados ......")
        except TypeError:
            return ("Erro ao excluir os arquivos")

    def process_columns(self):
        try:
            file_path = self.find_file()

            if file_path:
                self.data_frame = pd.read_excel(file_path, header=9, dtype={
                                                'CNPJ': str, f'NÚMERO': str, 'ENDEREÇO': str}, index_col=False)
                self.data_atual = datetime.datetime.now()
                self.mes_ano = self.data_atual.strftime("%m/%Y")
                self.data_frame = self.data_frame.assign(
                    MES=[self.mes_ano]*len(self.data_frame))

                self.semana = self.data_atual.strftime(
                    "%d/%m/%y") + ' - ' + (self.data_atual + datetime.timedelta(days=6)).strftime("%d/%m/%y")
                self.data_frame = self.data_frame.assign(SEMANA=self.semana)

                self.data_frame['ENDEREÇO_PPB'] = self.data_frame['ENDEREÇO'] + \
                    ' ' + self.data_frame['NÚMERO']

                print("deletando colunas")
                for colun in colluns_to_drop:
                    del self.data_frame[colun]

                print("criando colunas")
                for column_name in createe_colluns:
                    self.data_frame[column_name] = 0

                print("Renomeando colunas")
                self.data_frame = self.data_frame.rename(
                    columns=colluns_rename)
            else:
                print("falha ao achar as colunas.")
        except TypeError:
            return ("Erro ao processar o arquivo")

    def insert_columns_data(self):
        print("Trabalhando nos dados da tabela")
        self.data_frame['CODIGO_FONTE_PESQUISA'] = 1
        self.data_frame['FONTE_PESQUISA'] = "Anp"

        # transforma em camel case
        for coluna in colluns_camel:
            self.data_frame[coluna] = self.data_frame[coluna].apply(lambda x: ''.join(
                word.title() for word in str(x).split('_')) if isinstance(x, str) else x)
         # remove os acentos
        for coluna in colluns_camel:
            self.data_frame[coluna] = self.data_frame[coluna].apply(
                lambda x: unidecode(x) if isinstance(x, str) else x)
        self.data_frame['PRODUTO_PPB'] = self.data_frame['PRODUTO'].map(
            product_mapping).fillna(self.data_frame['PRODUTO_PPB'])
        del self.data_frame['PRODUTO']

        self.data_frame['GRUPO_BANDEIRA_PPB'] = self.data_frame['BANDEIRA'].map(
            brand_mapping).fillna(self.data_frame['GRUPO_BANDEIRA_PPB'])
        self.data_frame['UF_PPB'] = self.data_frame['ESTADO_PPB'].map(
            region_mapping).fillna(self.data_frame['UF_PPB'])

        self.data_frame['BAIRRO_PPB'] = self.data_frame['BAIRRO_PPB'].astype(
            str).str.replace(',', '')
        self.data_frame['ENDEREÇO_PPB'] = self.data_frame['ENDEREÇO_PPB'].astype(
            str).str.replace(',', '')
        self.data_frame['MUNICÍPIO_PPB'] = self.data_frame['MUNICÍPIO_PPB'].astype(
            str).str.replace(',', '')

        print("Montando ordem das colunas")
        self.data_frame = self.data_frame.reindex(columns=colluns_ordem)
        del self.data_frame['ESTADO_PPB']

        print("Montando o arquivo_final......")

        self.data_frame.to_csv("base_pesquisa_preco.xls", index=False, sep=';')

        print("Arquivo final pronto para uso")


url_gov = "https://www.gov.br/anp/pt-br/assuntos/precos-e-defesa-da-concorrencia/precos/levantamento-de-precos-de-combustiveis-ultimas-semanas-pesquisadas"


scraper = WebScraper(url_gov)
scraper.scrape_website()
formatter = FormatSheet()
formatter.process_columns()
formatter.insert_columns_data()
formatter.exclude_undesired()
