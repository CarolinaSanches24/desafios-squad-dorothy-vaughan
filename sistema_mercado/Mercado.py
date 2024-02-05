# Importando a biblioteca abc
from abc import ABC, abstractmethod
from datetime import datetime

class Pessoa(ABC):
    def __init__(self, id, nome, telefone, endereco):
        self._id= id
        self._nome = nome
        self._telefone = telefone
        self._endereco = endereco
        
    @property
    def id(self):
        return self._id
        
    @property
    def nome(self):
        return self._nome
        
    @property
    def telefone (self):
        return self._telefone
    @property
    def endereco(self):
        return self._endereco

    # Método abstrato
    @abstractmethod
    def exibir_informacoes(self):
        pass
        
class Cliente(Pessoa):
    def __init__(self, id, nome, telefone, endereco):
        super().__init__(id, nome, telefone, endereco)
        
         # Método para exibir informações do cliente utilizando o método abstrato
    def exibir_informacoes(self):
        return f'Cliente: {self._nome}\nTelefone: {self._telefone}\nEndereço: {self._endereco}'        
            
class Mercado():
    def __init__(self):
        self.__lista_clientes = []
        self.lista_produtos = []
        self.__lista_transacoes = []
        
    @property 
    def lista_transacoes(self):
        return self.__lista_transacoes
    
    def adicionar_cliente(self,cliente):
        self.__lista_clientes.append(cliente)
        
    def mostrar_clientes(self):
        for cliente in self.__lista_clientes:
            cliente = {
                "Nome":{cliente.nome},
                "Telefone":{cliente.telefone},
                "Endereço":{cliente.endereco}
            }
            print(cliente)
            
    def adicionar_produto(self,produto):
        self.lista_produtos.append(produto)
    
    def mostrar_produtos(self):
        for produto in self.lista_produtos:
            print(produto)
        
    def mostrar_transacoes (self):
        for transacao in self.__lista_transacoes:
            print(transacao)
            
    def vender_produto(self, produto, cliente, quantidade):

        # Fazendo algumas verificações utilizando o conceito de tratamento de exceções:        
        try:
            if produto not in self.lista_produtos:
                raise ValueError('Produto não encontrado no mercado.')
            if cliente not in self.__lista_clientes:
                raise ValueError('Cliente não registrado no mercado.')
            if quantidade <= 0:
                raise ValueError('A quantidade deve ser maior que zero.')
            if quantidade > produto.quantidade_produtos:
                raise ValueError('Quantidade insuficiente de produtos.')

            # Se tudo estiver certo, realiza a venda
            produto.quantidade_produtos -= quantidade
            transacao = Transacao(cliente._id, cliente._nome, produto.nome, quantidade)
            self.__lista_transacoes.append(transacao)
            print(f"Compra realizada: {quantidade} unidades de {produto.nome}")
        except ValueError as e:
            print(f'Erro ao vender produto: {str(e)}') 
        
    
            
class Produto:
    def __init__(self, id_produto, nome_produto, quantidade_produtos):
        self.id_produto = id_produto
        self.nome = nome_produto
        self.categoria = []
        self._quantidade_produtos = quantidade_produtos
        self.fornecedores =[]
    
    def adicionar_fornecedor(self, fornecedor):
        self.fornecedores.append(fornecedor)
    
    def adicionar_categoria(self, categoria):
        self.categoria.append(categoria)
        
    @property
    def quantidade_produtos(self):
        return self._quantidade_produtos

    @quantidade_produtos.setter
    def quantidade_produtos(self, nova_quantidade):
        self._quantidade_produtos = nova_quantidade    
        
    def __str__(self):
        return (
                f'ID:{self.id_produto}, Nome:{self.nome},'
                f' Quantidade:{self.quantidade_produtos}'
                f' Categorias: {self.categoria}'
                f' Fornecedores:{self.fornecedores}')
        
class Transacao:
    def __init__(self, id_cliente, nome_cliente, produtos, quantidade):
        self._id_cliente = id_cliente
        self._nome_cliente = nome_cliente
        self._produtos = produtos
        self._quantidade = quantidade
        self.data_da_compra = datetime.now()
    
    def __str__(self):
        data_formatada = self.data_da_compra.strftime('%d %m %Y %H:%M')
        return (f'ID: {self._id_cliente}\n'
                f' Nome Cliente : {self._nome_cliente}\n'
                f' Produtos : {self._produtos}\n'
                f' Quantidade:{self._quantidade}\n'
                f' Data da Compra: {data_formatada}\n'
                )
   
     
mercado = Mercado()
cliente1 = Cliente(1,"Clarice", 87879494, "Campina Grande")
print(cliente1.exibir_informacoes())
cliente2 = Cliente(2,"Carol",78459682,"Novo Buritizal")
mercado.adicionar_cliente(cliente1)
mercado.adicionar_cliente(cliente2)
produto1 = Produto(1,"Arroz",50)
produto1.adicionar_categoria("Carboidratos")
produto1.adicionar_fornecedor("Comercial Norte Distribuição")
mercado.adicionar_produto(produto1)

produto2 = Produto(2,"Feijão",10)
produto2.adicionar_categoria("Proteina")
produto2.adicionar_fornecedor("Comercial Norte Distribuição")
mercado.adicionar_produto(produto2)

mercado.vender_produto(produto1, cliente1, 10)
mercado.vender_produto(produto2, cliente1, 5)
mercado.vender_produto(produto2, cliente1, 10)
#estoque do produto apos compras do cliente
print(f'Estoque do produto\n {produto1}')
print(f'Estoque do produto\n {produto2}')

mercado.mostrar_transacoes()
mercado.mostrar_clientes()
mercado.mostrar_produtos()