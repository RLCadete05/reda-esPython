import re

import requests
from bs4 import BeautifulSoup

# verificar se a página está disponível
def get_pagina_existente(url):
    content = requests.get(url.strip())
    return False if content.status_code == 404 else content.content

#ainda n funciona
def temas_e_links(url):
    soup = BeautifulSoup(get_pagina_existente(url), 'lxml')
    #select = soup.find('select', attrs={'id': 'selectBoxBR'})
    options = soup.select('select[class=thumbnails-wrapper]> option')
    for option in options[1:]:
        print("TEMAS: ", option['value'] + '->' + option.link)

        
def get_descricao_tema(url):
    soup = BeautifulSoup(get_pagina_existente(url), 'lxml')
    description = soup.find('span', attrs={'class': 'text'})
    spans = description.find_all('span')#Erro com find_all
    print(spans[11].description)


def extrair_titulo_e_tema(url):
    soup = BeautifulSoup(get_pagina_existente(url), 'lxml')
    #print(soup.find('p', attrs={'class': 'text-composition'}))
    '''try:
        theme = soup.find_all('div', attrs={'class': 'container-composition'}).h2
        print('TEMA: ', theme)
    except Exception as e:
        try:
            theme = soup.find('p', attrs={'class': 'gmail-paragraph'})
            theme = theme.find('span').text.strip()
            print(theme)
        except Exception as e:
            print(e)'''
    print('TEMA: ', soup.find('div', attrs={'class': 'container-composition'}).h2)
    title = soup.find('div', attrs={'class': 'container-composition'})
    title = title.find('h2').text.strip()
    print('\nTITULO: ', title)
    essay = soup.find('div', attrs={'class': 'text-composition'})
    for content in essay.find_all('p')[0:]:
        print('\nREDAÇÃO: ', content.text)

def get_redacoes(url):
    soup = BeautifulSoup(get_pagina_existente(url), 'lxml')
    print('\nNOTA FINAL: ', soup.find('article', attrs={'class': 'rt-body'}).text)



URL_BASE = 'https://educacao.uol.com.br/bancoderedacoes/'
url_theme = 'https://educacao.uol.com.br/bancoderedacoes/propostas/qualificacao-e-o-futuro-do-emprego.htm'
url_essay = 'https://educacao.uol.com.br/bancoderedacoes/redacoes/qualificacoes-para-o-mercado-de-trabalho.htm'

temas_e_links(URL_BASE)
#get_descricao_tema(url_theme)
#get_redacoes(url_theme)

#extrair_titulo_e_tema(url_essay)
get_redacoes(url_essay)
