import re

import requests
from bs4 import BeautifulSoup

# verificar se a página está disponível
def get_pagina_existente(url):
    content = requests.get(url.strip())
    return False if content.status_code == 404 else content.content

# def temas_e_links(url):
#     soup = BeautifulSoup(get_pagina_existente(url), 'lxml')
#     # select = soup.find('select', attrs={'id': 'selectBoxBR'})
#     options = soup.select('select[id=selectBoxBR]> option')
#     for option in options[1:]:
#         print(option['value'] + '->' + option.text)

# def get_descricao_tema(url):
#     soup = BeautifulSoup(get_pagina_existente(url), 'lxml')
#     secao_texto = soup.find('div', attrs={'id': 'secao_texto'})
#     divs = secao_texto.find_all('div')
#     print(divs[11].text)

# '''
# def get_essays(url):
#     soup = BeautifulSoup(get_pagina_existente(url), 'lxml')
#     tables = soup.find('table', attrs={'id': 'redacoes_corrigidas'})
#     links = tables.find_all('a')
#     for link in links:
#         print(link.get('href'))
# '''

# def extrair_titulo_e_tema(url):
#     soup = BeautifulSoup(get_pagina_existente(url), 'lxml')
#     try:
#         theme = soup.find_all('span', attrs={'itemprop': 'name'})[2].text
#         print('\nTEMA: ', theme)
#     except Exception as e:
#         try:
#             theme = soup.find('span', attrs={'class': 'definicao'})
#             theme = theme.find('a').text.strip()
#             print(theme)
#         except Exception as e:
#             print(e)
#     title = soup.find('div', attrs={'class': 'br-grid-3 margem-conteudo'})
#     title = title.find('h1').text.strip()
#     print('\nTITULO: ', title)

#     essay = soup.find('div', attrs={'class': 'conteudo-materia'})
#     for content in essay.find_all('p')[1:]:
#         print('\nREDAÇÃO: ', content.text)

# def get_redacoes(url):
#     soup = BeautifulSoup(get_pagina_existente(url), 'lxml')
#     tabela = soup.find('table', attrs={'id': 'redacoes_corrigidas'})
#     coluna = tabela.find_all('td')[1]
#     print(soup.find(id='redacoes_corrigidas').text)



def extrair_tema(url):
    try:
        soup = BeautifulSoup(get_pagina_existente(url), 'lxml')
        tema = soup.find('span', { 'class': 'definicao' }).text
        return tema.replace('Tema: ', '').strip()
    except:
        return 'Não possui tema'

def extrair_titulo(url):
    try:
        soup = BeautifulSoup(get_pagina_existente(url), 'lxml')
        titulo = soup.h1.text
        return titulo.strip()
    except:
        return 'Não possui título'

def extrair_redacao(url):
    try:
        soup = BeautifulSoup(get_pagina_existente(url), 'lxml')
        container = soup.find('div', { "class": "conteudo-materia" })
        texto_da_redacao = ''
        for redacao in container.find_all('p')[1:-3]:
            texto_da_redacao += redacao.text
        return texto_da_redacao.replace("'", "")
    except:
        return 'O texto não foi extraido devido ter aspas simples'

def extrair_nota(url):
    try:
        soup = BeautifulSoup(get_pagina_existente(url), 'lxml')
        competencias = soup.find(id='redacoes_corrigidas')
        notas = competencias.find_all('td', { 'style': 'text-align:center; border:solid 1px #cecece; border-left:none;' })
        notas_por_competencia = []
        for nota in notas:
            notas_por_competencia.append(float(nota.text.strip()))
        total = competencias.find(style='margin-right: 20px;').text.replace('NOTA FINAL:', '').strip()
        notas_por_competencia.append(float(total))
        return notas_por_competencia
    except:
        return [ 0 ]

def pegar_redacao(url):
    tema = extrair_tema(url)
    titulo = extrair_titulo(url)
    texto_da_redacao = extrair_redacao(url)
    notas = extrair_nota(url)
    return [tema, titulo, texto_da_redacao, notas]

# URL_BASE = 'https://vestibular.brasilescola.uol.com.br/banco-de-redacoes'
# url_tema = 'https://vestibular.brasilescola.uol.com.br/banco-de-redacoes/tema-abuso-de-autoridade-no-brasil.htm'
# url_redacao = 'https://vestibular.brasilescola.uol.com.br/banco-de-redacoes/16257'
# temas_e_links(URL_BASE)
# get_descricao_tema(url_tema)
# extrair_titulo_e_tema(url_redacao)
# get_redacoes(url_redacao)

# extrair_tema(url_tema)
# extrair_titulo(url_redacao)
# extrair_redacao(url_redacao)
# extrair_nota(url_redacao)


# extrair titulo
# extrair tema
# extrair redação
# extrair nota
# tema = 'Violência contra a mulher: por que o machismo persiste?'
# titulo = 'INVOLUÇÃO HUMANA: MACHISMO E VIOLÊNCIA CONTRA A MULHER'

# return [tema, titulo]
# retorno da função: [tema, titulo, redacao, nota]


