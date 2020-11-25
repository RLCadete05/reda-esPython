import psycopg2

# Por padrão utilizará estes valores, mas caso seja outros, só modificar quando for chamar a função
def conectar(host='localhost', database='redacoes', user='pguser', password='pgpassword'):
  try:
    # Retorna a conexão com o banco postgres
    # Essa conexão é utilizada pelas outras funções
    return psycopg2.connect(host=host, database=database, user=user, password=password)
  except:
    # Caso não conecte, vai retornar falso e não executara as outras funções
    print('Verifique os dados da conexão com o banco')
    return False

# Por padrão cria a tabela redação, mas basta passar outros valores para a função
def criar_tabela(tabela="redacao", colunas="id serial primary key, titulo varchar(255), textoRedacao varchar(255)"):
  # Conectando ao banco
  conexao = conectar()
  # Caso ocorra erro na conexão com o banco, nem executará o resto da função
  if(not conexao):
    return 'Erro na conexão com o banco'
  
  if(tabela and colunas):
    # Tenta criar a tabela
    try:
      sql_da_criacao_da_tabela = "create table {} ({})".format(tabela, colunas)
      cursor = conexao.cursor()
      cursor.execute(sql_da_criacao_da_tabela)
      conexao.commit() #
      cursor.close()
      return 'Criada com sucesso'
    # Erro de sintaxe
    except psycopg2.errors.SyntaxError:
      return 'Erro no sql'
    # Caso a tabela já exista, vai retornar essa mensagem
    except:
      return 'A tabela já existe'
  # Caso não seja informado os parâmetros
  else:
    return 'Informe a tabela e/ou colunas da nova tabela'


# Por padrão insere na tabela redação, porém basta passar outra quando chamar a função
def inserir_na_tabela(tabela="redacao", valores="default,'Problemas no Piauí','O problema foi devido a falta de água'"):
  # Conectando ao banco
  conexao = conectar()
  # Caso ocorra erro na conexão com o banco, nem executará o resto da função
  if(not conexao):
    return 'Erro na conexão com o banco'

  if(tabela and valores):

    # Tenta inserir na tabela
    # try:
      sql_da_insercao = "insert into {} values ({})".format(tabela, valores)
      cursor = conexao.cursor()
      cursor.execute(sql_da_insercao)
      conexao.commit()
      cursor.close()
      return 'Inserido com sucesso'
    # Caso o sql informado esteja errado, retorna essa mensagem
    # except:
    #   return 'Erro ao inserir, verifique seu sql'
  else:
    return 'Tabela e/ou valores inválidos'

# Por padrão lista todos os dados da tabela redacao
def listar_dados_da_tabela(tabela="redacao", condicao="*"):
   # Conectando ao banco
  conexao = conectar()
  # Caso ocorra erro na conexão com o banco, nem executará o resto da função
  if(not conexao):
    return 'Erro na conexão com o banco'
  # Se for informado a tabela e a condição
  if(tabela and condicao):

    # Tenta retornar os dados da tabela
    try:
      # Sql da select
      sql_da_selecao = 'select {} from {}'.format(condicao, tabela)
      # Cria uma ação
      cursor = conexao.cursor()
      # Executa uma ação, passando o comando sql
      cursor.execute(sql_da_selecao)
      # Retorna todo o resultado
      dados = cursor.fetchall()
      # Comenta o resultado
      conexao.commit()
      # Finaliza a ação
      cursor.close()
      # Retorna os dados
      return dados
    # Caso o sql informado esteja errado, retorna essa mensagem
    except:
      return 'Erro ao listar dados da tabela, verifique a condição (query) e/ou tabela informada'
  else:
    return 'Informe a tabela e/ou condição para listar a tabela'

def deletar_tabela(tabela="redacao"):
   # Conectando ao banco
  conexao = conectar()
  # Caso ocorra erro na conexão com o banco, nem executará o resto da função
  if(not conexao):
    return 'Erro na conexão com o banco'
  # Se for informado a tabela e a condição
  if(tabela):

    # Tenta deletar a tabela
    try:
      # Sql da remoção
      sql_da_remocao = 'DROP TABLE {}'.format(tabela)
      # Cria uma ação
      cursor = conexao.cursor()
      # Executa uma ação, passando o comando sql
      cursor.execute(sql_da_remocao)
      # Comenta o resultado
      conexao.commit()
      # Finaliza a ação
      cursor.close()
      # Retorna os dados
      return 'Removido com sucesso'
    # Caso o sql informado esteja errado, retorna essa mensagem
    except:
      return 'Erro ao deletar a tabela.'
  else:
    return 'Informe a tabela e/ou condição para listar a tabela'



