import re

import requests
from bs4 import BeautifulSoup

# verificar se a página está disponível
def get_pagina_existente(url):
    content = requests.get(url.strip())
    return False if content.status_code == 404 else content.content

def temas_e_links(url):
    soup = BeautifulSoup(get_pagina_existente(url), 'lxml')
    # select = soup.find('select', attrs={'id': 'selectBoxBR'})
    options = soup.select('select[id=selectBoxBR]> option')
    for option in options[1:]:
        print(option['value'] + '->' + option.text)

def get_descricao_tema(url):
    soup = BeautifulSoup(get_pagina_existente(url), 'lxml')
    secao_texto = soup.find('div', attrs={'id': 'secao_texto'})
    divs = secao_texto.find_all('div')
    print(divs[11].text)

'''
def get_essays(url):
    soup = BeautifulSoup(get_pagina_existente(url), 'lxml')
    tables = soup.find('table', attrs={'id': 'redacoes_corrigidas'})
    links = tables.find_all('a')
    for link in links:
        print(link.get('href'))
'''

def extrair_titulo_e_tema(url):
    soup = BeautifulSoup(get_pagina_existente(url), 'lxml')
    try:
        theme = soup.find_all('span', attrs={'itemprop': 'name'})[2].text
        print('\nTEMA: ', theme)
    except Exception as e:
        try:
            theme = soup.find('span', attrs={'class': 'definicao'})
            theme = theme.find('a').text.strip()
            print(theme)
        except Exception as e:
            print(e)
    title = soup.find('div', attrs={'class': 'br-grid-3 margem-conteudo'})
    title = title.find('h1').text.strip()
    print('\nTITULO: ', title)

    essay = soup.find('div', attrs={'class': 'conteudo-materia'})
    for content in essay.find_all('p')[1:]:
        print('\nREDAÇÃO: ', content.text)

def get_redacoes(url):
    soup = BeautifulSoup(get_pagina_existente(url), 'lxml')
    tabela = soup.find('table', attrs={'id': 'redacoes_corrigidas'})
    coluna = tabela.find_all('td')[1]
    print(soup.find(id='redacoes_corrigidas').text)



def extrair_tema(url): 
    soup = BeautifulSoup(get_pagina_existente(url), 'lxml')
    tema = soup.find_all('span', attrs={'class': 'definicao'})
    #tema = tema.find('a').text.strip()
    print(tema)

def extrair_titulo(url):
    soup = BeautifulSoup(get_pagina_existente(url), 'lxml')
    titulo = soup.find('div', attrs={'class': 'br-grid-3 margem-conteudo'})
    titulo = titulo.find('h1').text.strip()
    print('\nTITULO: ', titulo)

def extrair_redacao(url): 
    soup = BeautifulSoup(get_pagina_existente(url), 'lxml')
    essay = soup.find('div', attrs={'class': 'conteudo-materia'})
    for content in essay.find_all('p')[1:]:
        print(content.text)

def extrair_nota(url):
    soup = BeautifulSoup(get_pagina_existente(url), 'lxml')
    tabela = soup.find('table', attrs={'id': 'redacoes_corrigidas'})
    coluna = tabela.find_all('td')[1]
    print(soup.find(id='redacoes_corrigidas').text)




URL_BASE = 'https://vestibular.brasilescola.uol.com.br/banco-de-redacoes'
url_tema = 'https://vestibular.brasilescola.uol.com.br/banco-de-redacoes/tema-abuso-de-autoridade-no-brasil.htm'
url_redacao = 'https://vestibular.brasilescola.uol.com.br/banco-de-redacoes/16257'
# temas_e_links(URL_BASE)
# get_descricao_tema(url_tema)
# extrair_titulo_e_tema(url_redacao)
# get_redacoes(url_redacao)

extrair_tema(url_tema)
extrair_titulo(url_redacao)
extrair_redacao(url_redacao)
extrair_nota(url_redacao)


# extrair titulo
# extrair tema
# extrair redação
# extrair nota
# tema = 'Violência contra a mulher: por que o machismo persiste?'
# titulo = 'INVOLUÇÃO HUMANA: MACHISMO E VIOLÊNCIA CONTRA A MULHER'

# return [tema, titulo]
# retorno da função: [tema, titulo, redacao, nota]


