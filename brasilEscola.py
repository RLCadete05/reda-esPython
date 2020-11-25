import re

import requests
from bs4 import BeautifulSoup

# verificar se a página está disponível
def get_pagina_existente(url):
    content = requests.get(url.strip())
    return False if content.status_code == 404 else content.content

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
