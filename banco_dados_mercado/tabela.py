import sqlite3

conexao = sqlite3.connect('mercado.bd')
cursor = conexao.cursor()

cursor.execute('CREATE TABLE clientes(id_cliente int primary key, nome_cliente varchar(100), telefone_cliente int, endereco_cliente varchar(100))')
cursor.execute('CREATE TABLE produtos(id_produto int primary key, nome_produto varchar(100), categoria_produto varchar(50), qtde_produto int, fornecedor_produto varchar(100))')
##cursor.execute('CREATE TABLE transacao(dt_compra date, )




conexao.commit()
conexao.close()
