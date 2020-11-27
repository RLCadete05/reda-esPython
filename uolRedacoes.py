import re

import requests
from bs4 import BeautifulSoup

# verificar se a página está disponível
def get_pagina_existente(url):
    content = requests.get(url.strip())
    return False if content.status_code == 404 else content.content

def get_link_dos_temas():
    soup = BeautifulSoup(get_pagina_existente('https://educacao.uol.com.br/bancoderedacoes/'), 'lxml')
    temas = soup.select('.thumbnails-wrapper > a')
    links_dos_temas = []
    for tema in temas:
        links_dos_temas.append(tema.get('href'))
    return links_dos_temas


def get_propostas(url):
    soup = BeautifulSoup(get_pagina_existente(url), 'lxml')
    propostas = soup.select('.rt-line-option > a')
    links_das_propostas = []
    for proposta in propostas:
        links_das_propostas.append(proposta.get('href'))
    return links_das_propostas


def get_redacao(url):
    soup = BeautifulSoup(get_pagina_existente(url), 'lxml')
    tema = soup.select('.custom-title')[0].text
    titulo = soup.select('.container-composition > h2')[0].text
    paragrafos_da_redacao = soup.select('.text-composition > P')
    redacao_completa = ''
    for redacao in paragrafos_da_redacao:
        redacao_completa += redacao.text
    notas = soup.select('.points')[:6]
    lista_de_notas = []
    for nota in notas:
        lista_de_notas.append(float(nota.text))
    return [tema.replace("'", "`"), titulo.replace("'", "`"), redacao_completa.replace("'", "`"), lista_de_notas]


def get_todas_as_redacoes():
    temas = get_link_dos_temas()
    lista_de_redacoes = []
    index = 0
    for tema in temas:
        propostas = get_propostas(tema)
        for proposta in propostas:
            index += 1
            print(index)
            lista_de_redacoes.append(get_redacao(proposta))
    return lista_de_redacoes


