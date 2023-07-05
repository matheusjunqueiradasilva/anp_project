from setuptools import setup

setup(
    name="anp_projeto",
    version='1.0',
    description='Este é um projeto de web scraping desenvolvido para coletar dados do levantamento de preços de combustíveis da Agência Nacional do Petróleo, Gás Natural e Biocombustíveis (ANP) referentes à distribuidora Ipiranga. O script Python utiliza a biblioteca BeautifulSoup para fazer a raspagem dos dados do site da ANP e o pandas para manipulação e formatação dos dados coletados.',
    author='Matheus Junqueira da Silva',
    packages=['anp_projeto'],
    requires=['bs4', 'requests', 'pandas',
              'glob', 'os', 'datetime', 'settings']

)
