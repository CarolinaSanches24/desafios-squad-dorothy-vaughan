from datetime import datetime
#Modelagem inicial, aberta a mudanças
class Cliente():
    def __init__(self, id_cliente, nome_cliente, telefone_cliente, endereco_cliente):
        self._id_cliente = id_cliente
        self._nome = nome_cliente
        self._telefone = telefone_cliente
        self._endereco = endereco_cliente
    #Método para exibir informações do cliente
    def __str__(self):
        return f'Cliente: {self._nome}\nTelefone: {self._telefone}\nEndereço: {self._endereco}'
            
class Produto:
    def __init__(self, nome_produto, quantidade_produtos):
        self.nome = nome_produto
        self.categoria = []
        self.quantidade = quantidade_produtos
        self.fornecedores =[]
        self.lista_produtos = [];
    
    def adicionar_produto(self):
        dados_produto = {
            'nome': self.nome,
            'quantidade':self.quantidade,
            'categoria':self.categoria,
            'fornecedores':self.fornecedores
        }
        self.lista_produtos.append(dados_produto);
    
    def adicionar_fornecedor(self, fornecedor):
        self.fornecedores.append(fornecedor);
    
    def adicionar_categoria(self, categoria):
        self.categoria.append(categoria)
class Transacao:
    def __init__(self, cliente, produtos):
        self._cliente = cliente
        self._produtos = produtos
        self.data_da_compra = datetime.now();
        self.lista_transacoes = [];
       
    def realizar_compra(self):
        
        # sujeito a alterações e melhorias
        data_formatada = self.data_da_compra.strftime('%d %m %Y %H:%M');
        
        dados_transacao = {
            'data_da_compra':data_formatada,
            'cliente': self._cliente,
            'produtos':self._produtos
        }
        self.lista_transacoes.append(dados_transacao);
cliente1 = Cliente(1,"Clarice", 87879494, "Campina Grande")
# print(cliente1)

produto1 = Produto("Camisa Azul",50);
produto1.adicionar_categoria("Roupas");
produto1.adicionar_fornecedor("Lojas Marisa")
produto1.adicionar_produto();

# Lista de produtos
for produto in produto1.lista_produtos:
    print(produto)

# Lista de transacoes
array_produtos = ["Camisa Azul", 5];
trasacao1 = Transacao("Clarice", array_produtos);
trasacao1.realizar_compra();
for trasacao in trasacao1.lista_transacoes:
    print(trasacao);