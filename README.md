# Projeto ANP da Ipiranga

Este é um projeto de web scraping desenvolvido para coletar dados do levantamento de preços de combustíveis da Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) referentes à distribuidora Ipiranga. O script Python utiliza a biblioteca BeautifulSoup para fazer a raspagem dos dados do site da ANP e o pandas para manipulação e formatação dos dados coletados.

## Funcionalidades

Web Scraping: O código utiliza a biblioteca BeautifulSoup para realizar o scraping de um site especificado pela URL url_gov. Ele baixa os arquivos encontrados nos links presentes nas listas do site.

Formatação de Planilha: O código utiliza a biblioteca Pandas para ler um arquivo Excel baixado anteriormente e realizar transformações nos dados. Ele remove colunas indesejadas, cria novas colunas, renomeia colunas existentes e formata os valores das colunas de acordo com mapeamentos definidos.

Tratamento de Dados: O código realiza tratamentos adicionais nos dados, como a remoção de acentos e substituição de caracteres especiais em algumas colunas. Além disso, ele mapeia valores específicos em determinadas colunas, substituindo-os por valores predefinidos.

Geração de Arquivo Final: Após as transformações nos dados, o código gera um arquivo final no formato CSV, chamado base_pesquisa_preco.xls, contendo os dados formatados e pronto para uso.

## Como Executar

1. **Instalação de Dependências:** Antes de executar o código, é necessário ter o Python instalado em sua máquina. Além disso, é necessário instalar as bibliotecas `BeautifulSoup` e `pandas`. Isso pode ser feito usando o `pip`. Abra o terminal e execute os seguintes comandos:
obs: voce precisa estar no mesmo diretório do requirements.txt

```
pip install -r requirements.txt
```

2. **Configuração e Execução:** Antes de executar o código, certifique-se de ter os arquivos `settings.py` no mesmo diretório do script principal. O arquivo `settings.py` tem as configurações necessárias, como as colunas do arquivo final e o caminho para o diretório onde os arquivos baixados serão salvos.

3. **URL para Scraping:** O web scraper foi desenvolvido para extrair dados de uma URL específica. Certifique-se de que a URL fornecida no código principal (variável `url_gov`) ainda esteja válida e corresponda à página com os dados de preços de combustíveis que você deseja extrair.

4. **Execução do Código:** Após instalar as dependências e configurar o ambiente, execute o script principal (código fornecido) em seu ambiente Python.

