from Redacoes import Redacoes
import requests
from bs4 import BeautifulSoup


class BrasilEscola(Redacoes):
  def __init__(self, titulo='', html='', notas=''):
    super().__init__(titulo, html, notas)
  
  def extrairTema(self, url):
    try:
        soup = BeautifulSoup(self.getPaginaExistente(url), 'lxml')
        tema = soup.find('span', { 'class': 'definicao' }).text
        return tema.replace('Tema: ', '').strip()
    except:
        return 'Não possui tema'

  def extrairTitulo(self, url):
    try:
        soup = BeautifulSoup(self.getPaginaExistente(url), 'lxml')
        titulo = soup.h1.text
        return titulo.strip()
    except:
        return 'Não possui título'

  def extrairRedacao(self, url):
    try:
        soup = BeautifulSoup(self.getPaginaExistente(url), 'lxml')
        container = soup.find('div', { "class": "conteudo-materia" })
        texto_da_redacao = ''
        for redacao in container.find_all('p')[1:-3]:
            texto_da_redacao += '{}'.format(redacao)
        return texto_da_redacao.replace("'", "`")
    except:
        return 'O texto não foi extraido devido ter aspas simples'

  def extrairNota(self, url):
    try:
        soup = BeautifulSoup(self.getPaginaExistente(url), 'lxml')
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

  def getRedacao(self, url):
    tema = self.extrairTema(url)
    titulo = self.extrairTitulo(url)
    texto_da_redacao = self.extrairRedacao(url)
    notas = self.extrairNota(url)
    return [tema, titulo, texto_da_redacao, notas]
