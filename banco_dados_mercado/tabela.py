import sqlite3

conexao = sqlite3.connect('mercado')
cursor = conexao.cursor()

# cursor.execute('CREATE TABLE clientes(id_cliente int primary key, nome_cliente varchar(100), telefone_cliente varchar(20), endereco_cliente varchar(100))')
# cursor.execute('CREATE TABLE produtos(id_produto int primary key, nome_produto varchar(100), categoria_produto varchar(50), qtde_produto int, valor_produto money, fornecedor_produto varchar(100))')
# cursor.execute('CREATE TABLE transacoes(id_transacao int primary key, dt_compra DATE, qtde_comprada int, id_cliente int, id_produto int, FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente), FOREIGN KEY (id_produto) REFERENCES produtos(id_produto))')


# cursor.execute('insert into clientes(id_cliente, nome_cliente, telefone_cliente, endereco_cliente) values (1, "Ana", "12344321", "rua flores") ')
# cursor.execute('insert into clientes(id_cliente, nome_cliente, telefone_cliente, endereco_cliente) values (2, "Maite", "12344377", "rua jardim")')
# cursor.execute('insert into clientes(id_cliente, nome_cliente, telefone_cliente, endereco_cliente) values (3, "Simone", "34544321", "rua rosas")')
# cursor.execute('insert into clientes(id_cliente, nome_cliente, telefone_cliente, endereco_cliente) values (4, "Jane", "12355321", "rua margaridas")')
# cursor.execute('insert into clientes(id_cliente, nome_cliente, telefone_cliente, endereco_cliente) values (5, "Isadora", "12346661", "rua tulipa")')
# cursor.execute('insert into clientes(id_cliente, nome_cliente, telefone_cliente, endereco_cliente) values (6, "Carolina", "84237428", "passarela 13")')

# cursor.execute('insert into produtos(id_produto, nome_produto, categoria_produto, qtde_produto, valor_produto, fornecedor_produto) values (1, "sabao limpinho", "limpeza", 10, 5.00, "triex")')
# cursor.execute('insert into produtos(id_produto, nome_produto, categoria_produto, qtde_produto, valor_produto, fornecedor_produto) values (2, "arroz", "mercado", 18, 15.00, "camil")')
# cursor.execute('insert into produtos(id_produto, nome_produto, categoria_produto, qtde_produto, valor_produto, fornecedor_produto) values (3, "arroz", "mercado", 10, 18.00, "panela de ferro")')
# cursor.execute('insert into produtos(id_produto, nome_produto, categoria_produto, qtde_produto, valor_produto, fornecedor_produto) values (4, "bolacha piraque", "biscoitos", 13, 4.50, "piraque")')
# cursor.execute('insert into produtos(id_produto, nome_produto, categoria_produto, qtde_produto, valor_produto, fornecedor_produto) values (5, "coca cola", "bebidas", 15, 9.00, "ambev")')

# cursor.execute('insert into transacoes(id_transacao, dt_compra, qtde_comprada, id_produto, id_cliente) values (1, "2024-01-01", 1, 1, 2)')
# cursor.execute('insert into transacoes(id_transacao, dt_compra, qtde_comprada, id_produto, id_cliente) values (2, "2024-02-01", 3, 4, 3)')
# cursor.execute('insert into transacoes(id_transacao, dt_compra, qtde_comprada, id_produto, id_cliente) values (3, "2024-01-14", 4, 5, 1)')
# cursor.execute('insert into transacoes(id_transacao, dt_compra, qtde_comprada, id_produto, id_cliente) values (4, "2024-02-02", 2, 2, 5)')
# cursor.execute('insert into transacoes(id_transacao, dt_compra, qtde_comprada, id_produto, id_cliente) values (5, "2024-01-17", 2, 2, 1)')


# Consultas SQL
# # Listar todos produtos em estoque:
estoque_mercado = cursor.execute('SELECT nome_produto,qtde_produto FROM produtos') 
for produtos in estoque_mercado:
   print(produtos)


# # Encontrar as compras realizadas por um cliente específico:
compras_cliente = cursor.execute('SELECT id_transacao, dt_compra FROM transacoes WHERE id_cliente=1')
for transacoes in compras_cliente:
   print(transacoes)


# # Calcular o total de vendas por categoria de produto:
categoria_produtos = {
    0 : "todas",
    1 : "limpeza",
    2 : "mercado",
    3 : "biscoitos",
    4 : "bebidas"
}

total_vendas = cursor.execute('SELECT SUM(qtde_comprada) FROM transacoes INNER JOIN produtos ON transacoes.id_produto=produtos.id_produto')
for produtos in total_vendas:
    print(f"Nosso mercado vendeu o total de {produtos} categoria {categoria_produtos[0]}")

total_vendas_limpeza = cursor.execute('SELECT SUM(qtde_comprada) FROM transacoes INNER JOIN produtos ON transacoes.id_produto=produtos.id_produto WHERE produtos.categoria_produto = "limpeza"')
for limpeza in total_vendas_limpeza:
    print(f"Nosso mercado vendeu o total de {limpeza} categoria {categoria_produtos[1]}")

total_vendas_mercado = cursor.execute('SELECT SUM(qtde_comprada) FROM transacoes INNER JOIN produtos ON transacoes.id_produto=produtos.id_produto WHERE produtos.categoria_produto = "mercado"')
for mercado in total_vendas_mercado:
    print(f"Nosso mercado vendeu o total de {mercado} categoria {categoria_produtos[2]}")

total_vendas_biscoitos = cursor.execute('SELECT SUM(qtde_comprada) FROM transacoes INNER JOIN produtos ON transacoes.id_produto=produtos.id_produto WHERE produtos.categoria_produto = "biscoitos"')
for biscoitos in total_vendas_biscoitos:
    print(f"Nosso mercado vendeu o total de {biscoitos} categoria {categoria_produtos[3]}")

total_vendas_bebidas = cursor.execute('SELECT SUM(qtde_comprada) FROM transacoes INNER JOIN produtos ON transacoes.id_produto=produtos.id_produto WHERE produtos.categoria_produto = "bebidas"')
for bebidas in total_vendas_bebidas:
    print(f"Nosso mercado vendeu o total de {bebidas} categoria {categoria_produtos[4]}")


# Identificar os produtos mais vendidos:
produtos_mais_vendidos = cursor.execute('SELECT * FROM transacoes ORDER BY qtde_comprada,id_produto')
for transacoes in produtos_mais_vendidos:
   print(transacoes)
  

# Atualizações e Exclusões
cursor.execute('UPDATE produtos SET qtde_produto = qtde_produto -3 WHERE id_produto = 1')
cursor.execute('UPDATE produtos SET valor_produto = 9.50 WHERE id_produto = 5')


cursor.execute('DELETE FROM clientes WHERE id_cliente = 2')

conexao.commit()
conexao.close()