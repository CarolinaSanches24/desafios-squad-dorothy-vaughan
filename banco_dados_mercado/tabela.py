import sqlite3

conexao = sqlite3.connect('mercado.bd')
cursor = conexao.cursor()

##cursor.execute('CREATE TABLE clientes(id_cliente int primary key not null, nome_cliente varchar(100) not null, telefone_cliente int, endereco_cliente varchar(100) not null)')
##cursor.execute('CREATE TABLE produtos(id_produto int primary key not null, nome_produto varchar(100) not null, categoria_produto varchar(50), qtde_produto int not null, fornecedor_produto varchar(100) not null)')
##cursor.execute('CREATE TABLE transacao(dt_compra date, )

cursor.execute('insert into clientes(id_cliente, nome_cliente, telefone_cliente, endereco_cliente) values (1, "Ana", 12344321, "rua flores") ')
cursor.execute('insert into clientes(id_cliente, nome_cliente, telefone_cliente, endereco_cliente) values (2, "Maite", 12344377, "rua jardim")')
cursor.execute('insert into clientes(id_cliente, nome_cliente, telefone_cliente, endereco_cliente) values (3, "Simone", 34544321, "rua rosas")')
cursor.execute('insert into clientes(id_cliente, nome_cliente, telefone_cliente, endereco_cliente) values (4, "Jane", 12355321, "rua margaridas")')
cursor.execute('insert into clientes(id_cliente, nome_cliente, telefone_cliente, endereco_cliente) values (5, "Isadora", 12346661, "rua tulipa")')
cursor.execute('insert into produtos(id_produto, nome_produto, categoria_produto, qtde_produto, fornecedor_produto) values (1, "sabao limpinho", "limpeza", 10, "triex")')



conexao.commit()
conexao.close()
