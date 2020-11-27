# Arquivo principal do sistema

import brasilEscola
import db
from uolRedacoes import get_todas_as_redacoes

db.conectar(host='localhost', database='redacoes', user='pguser', password='pgpassword')
# print(db.deletar_tabela())
print(db.criar_tabela('redacao', 'id serial primary key, titulo varchar, tema varchar, redacao varchar, nota real[]'))

# for numero in range(14000, 16000):
#   print(numero)
#   url = 'https://vestibular.brasilescola.uol.com.br/banco-de-redacoes/{}'.format(numero)
#   try:
#     tema = brasilEscola.extrair_tema(url)
#     titulo = brasilEscola.extrair_titulo(url)
#     texto_da_redacao = brasilEscola.extrair_redacao(url)
#     notas = brasilEscola.extrair_nota(url)
#     notas_texto = '{}'.format(notas).replace('[', '{').replace(']', '}')


#     sql = "default, '{}', '{}', '{}', '{}'".format(titulo, tema, texto_da_redacao, notas_texto)
#     print(db.inserir_na_tabela('redacao', sql))
#   except:
#     print('Não foi possivel adicionar a redação da página: ', numero)

redacoes = get_todas_as_redacoes()
for redacao in redacoes:
  tema = redacao[0]
  titulo = redacao[1]
  texto_da_redacao = redacao[2]
  notas = redacao[3]
  notas_texto = '{}'.format(notas).replace('[', '{').replace(']', '}')
  sql = "default, '{}', '{}', '{}', '{}'".format(titulo, tema, texto_da_redacao, notas_texto)
  print(db.inserir_na_tabela('redacao', sql))
  
