import os


caminho_bytes = os.getcwdb()
caminho_unicode = caminho_bytes.decode('utf-8')
caminho_formatado = caminho_unicode.replace('/', '\\')

createe_colluns = ["UF_PPB", "GRUPO_BANDEIRA_PPB", "POSTO_ANP",
                   "CODIGO_FONTE_PESQUISA", "FONTE_PESQUISA", "PREÇO_MÉDIO_COMPRA", "GRP_PROD_NV_4", "GRP_PROD_NV_3","PRODUTO_PPB"]

colluns_ordem = ["SEMANA", "MES", "BAIRRO_PPB", "ENDEREÇO_PPB", "MUNICÍPIO_PPB", "CNPJ_PPB", "ESTADO_PPB", "RAZÃO_SOCIAL_PPB", "UF_PPB", "GRP_PROD_NV_4", "GRP_PROD_NV_3",
                 "GRUPO_BANDEIRA_PPB", "BANDEIRA", "POSTO_ANP", "PRODUTO_PPB", "DATA_DA_COLETA", "CODIGO_FONTE_PESQUISA", "FONTE_PESQUISA", "PREÇO_MÉDIO_VENDA", "PREÇO_MÉDIO_COMPRA"]
colluns_to_drop = ["COMPLEMENTO", "CEP", "ENDEREÇO", "NÚMERO"]

colluns_camel = ["BAIRRO_PPB", "ENDEREÇO_PPB", "MUNICÍPIO_PPB", "RAZÃO_SOCIAL_PPB",
                 "BANDEIRA", "PRODUTO_PPB"]
colluns_rename = {'CNPJ': 'CNPJ_PPB',
                  'RAZÃO': 'RAZÃO_SOCIAL_PPB',
                  'BAIRRO': 'BAIRRO_PPB',
                  'MUNICÍPIO': 'MUNICÍPIO_PPB',
                  'ESTADO': 'ESTADO_PPB',
                  'UNIDADE DE MEDIDA': 'UNIDADE DE MEDIDA_PPB',
                  'PREÇO DE REVENDA': 'PREÇO_MÉDIO_VENDA',
                  'DATA DA COLETA': 'DATA_DA_COLETA'}

product_mapping = {
    'DIESEL S10': 'Oleo Diesel B S10 - Comum',
    'DIESEL S500': 'Oleo Diesel B S500 - Comum',
    'ETANOL': 'Etanol Hidratado Comum',
    'GASOLINA ADITIVADA': 'Gasolina C Aditivada',
    'GASOLINA COMUM': 'Gasolina C Comum',
    'GLP': 'Glp',
    'GNV': 'Gas Natural Veicular'
}

brand_mapping = {
    'Bandeira Branca': 1,
    'Raizen': 16,
    'Raizen Mime': 16,
    'Sabba': 16,
    'Petrobras Distribuidora S.A.': 3,
    'Ipiranga': 9,
    'Mime': 16
}

region_mapping = {
    'ACRE': 'AC',
    'ALAGOAS': 'AL',
    'AMAPA': 'AP',
    'AMAZONAS': 'AM',
    'BAHIA': 'BA',
    'CEARA': 'CE',
    'DISTRITO FEDERAL': 'DF',
    'ESPIRITO SANTO': 'ES',
    'GOIAS': 'GO',
    'MARANHAO': 'MA',
    'MATO GROSSO': 'MT',
    'MATO GROSSO DO SUL': 'MS',
    'MINAS GERAIS': 'MG',
    'PARA': 'PA',
    'PARAIBA': 'PB',
    'PARANA': 'PR',
    'PERNAMBUCO': 'PE',
    'PIAUI': 'PI',
    'RIO DE JANEIRO': 'RJ',
    'RIO GRANDE DO NORTE': 'RN',
    'RIO GRANDE DO SUL': 'RS',
    'RONDONIA': 'RO',
    'RORAIMA': 'RR',
    'SANTA CATARINA': 'SC',
    'SAO PAULO': 'SP',
    'SERGIPE': 'SE',
    'TOCANTINS': 'TO'
}
