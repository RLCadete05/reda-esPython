from Redacoes import Redacoes
import requests
from bs4 import BeautifulSoup

class Uol(Redacoes):
  def __init__(self, titulo='', html='', notas=''):
    super().__init__(titulo, html, notas)
  
  def getLinkDosTemas(self):
    soup = BeautifulSoup(self.getPaginaExistente('https://educacao.uol.com.br/bancoderedacoes/'), 'lxml')
    temas = soup.select('.thumbnails-wrapper > a')
    links_dos_temas = []
    for tema in temas:
      links_dos_temas.append(tema.get('href'))
    return links_dos_temas

  def getPropostas(self, url):
    soup = BeautifulSoup(self.getPaginaExistente(url), 'lxml')
    propostas = soup.select('.rt-line-option > a')
    links_das_propostas = []
    for proposta in propostas:
        links_das_propostas.append(proposta.get('href'))
    return links_das_propostas

  def getRedacao(self, url):
    soup = BeautifulSoup(self.getPaginaExistente(url), 'lxml')
    tema = soup.select('.custom-title')[0].text
    titulo = soup.select('.container-composition > h2')[0].text
    paragrafos_da_redacao = soup.select('.text-composition > P')
    redacao_completa = ''
    for redacao in paragrafos_da_redacao:
        redacao_completa += '{}'.format(redacao)
    notas = soup.select('.points')[:6]
    lista_de_notas = []
    for nota in notas:
        lista_de_notas.append(float(nota.text))
    return [tema.replace("'", "`"), titulo.replace("'", "`"), redacao_completa.replace("'", "`"), lista_de_notas]

  def getTodasAsRedacoes():
    temas = self.getLinkDosTemas()
    lista_de_redacoes = []
    index = 0
    for tema in temas:
        propostas = self.getPropostas(tema)
        for proposta in propostas:
            index += 1
            print(index)
            lista_de_redacoes.append(self.getRedacao(proposta))
    return lista_de_redacoes
