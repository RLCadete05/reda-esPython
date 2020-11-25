# Arquivo principal do sistema

# import brasilEscola;
import db

db.conectar(host='localhost', database='redacoes', user='pguser', password='pgpassword')
print(db.criar_tabela('redacao', 'id serial primary key, titulo varchar, tema varchar, redacao varchar[], nota real[]'))
# print(db.deletar_tabela())

for numero in range(0, 10000):
  url_redacoes = 'https://vestibular.brasilescola.uol.com.br/banco-de-redacoes/{}'.format(numero)
  