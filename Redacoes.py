import requests
from bs4 import BeautifulSoup

class Redacoes:
  def __init__(self, titulo, html, notas):
    self.titulo = titulo
    self.html = html
    self.notas = notas

  def getTitulo(self):
    return self.titulo
  
  def setTitulo(self, titulo):
    self.titulo = titulo
  
  def getHtml(self):
    return self.html
  
  def setHtml(self, html):
    self.html = html

  def getNotas(self):
    return self.notas
  
  def setNotas(self, notas):
    self.notas = notas

  def getPaginaExistente(self, url):
    content = requests.get(url.strip())
    return False if content.status_code == 404 else content.content

  