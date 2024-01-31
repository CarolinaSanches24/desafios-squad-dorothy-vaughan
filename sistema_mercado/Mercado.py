from datetime import datetime
#Modelagem inicial, aberta a mudanças
class Cliente():
    def __init__(self, id_cliente, nome_cliente, telefone_cliente, endereco_cliente):
        self._id_cliente = id_cliente
        self._nome = nome_cliente
        self._telefone = telefone_cliente
        self._endereco = endereco_cliente
        # aqui podemos implementar encapsulamento e deixar esse dados como private
        
         #Método para exibir informações do cliente
    def __str__(self):
        return f'Cliente: {self._nome}\nTelefone: {self._telefone}\nEndereço: {self._endereco}'

class Mercado():
    def __init__(self):
        self.__lista_clientes = [];
        self.lista_produtos = [];
        self.__lista_transacoes = [];
        
    def adicionar_cliente(self,cliente):
        self.__lista_clientes.append(cliente);
    def mostrar_clientes (self):
        for cliente in self.__lista_clientes:
            print(cliente)
            
    def adicionar_produto(self,produto):
        self.lista_produtos.append(produto);
    
    def mostrar_produtos(self):
        for produto in self.lista_produtos:
            print(produto)
            
    def adicionar_transacao (self, transacao):
        self.__lista_transacoes.append(transacao);
        
    def mostrar_transacoes (self):
        for transacao in self.__lista_transacoes:
            print(transacao)
            
class Produto:
    def __init__(self, id_produto, nome_produto, quantidade_produtos):
        self.id_produto = id_produto;
        self.nome = nome_produto
        self.categoria = []
        self.quantidade_produtos = quantidade_produtos;
        self.fornecedores =[]
    
    def adicionar_fornecedor(self, fornecedor):
        self.fornecedores.append(fornecedor);
    
    def adicionar_categoria(self, categoria):
        self.categoria.append(categoria)
        
    def __str__(self):
        return (f'ID:{self.id_produto}, Nome:{self.nome},'
                f' Quantidade:{self.quantidade_produtos}'
                f' Categorias: {self.categoria}'
                f' Fornecedores:{self.fornecedores}')
        
class Transacao:
    def __init__(self, id_cliente, nome_cliente, produtos):
        self._id_cliente = id_cliente;
        self._nome_cliente = nome_cliente;
        self._produtos = produtos
        self.data_da_compra = datetime.now();
    
    def __str__(self):
        data_formatada = self.data_da_compra.strftime('%d %m %Y %H:%M');
        return (f'ID: {self._id_cliente}'
                f' Nome Cliente : {self._nome_cliente}'
                f' Produtos : {self._produtos}'
                f' Data da Compra: {data_formatada}'
                )
   
     
mercado = Mercado();
cliente1 = Cliente(1,"Clarice", 87879494, "Campina Grande")
# print(cliente1)

produto1 = Produto(1,"Arroz",50);
produto1.adicionar_categoria("Carboidratos");
produto1.adicionar_fornecedor("Comercial Norte Distribuição")

produto2 = Produto(2,"Feijão",10);
produto2.adicionar_categoria("Proteina");
produto2.adicionar_fornecedor("Comercial Norte Distribuição")

# ainda falta aprimorar a logica da transacao sintam-se a vontade para modificar
produtos_comprados = [(1,5), (2,3)] # id_produto e #quantidade
transacao1 = Transacao(1,"Clarice",produtos_comprados);
mercado.adicionar_transacao(transacao1);
mercado.mostrar_transacoes();

mercado.adicionar_cliente(cliente1);
mercado.mostrar_clientes();

mercado.adicionar_produto(produto1);
mercado.mostrar_produtos();