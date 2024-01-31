from datetime import datetime
#Modelagem inicial, aberta a mudanças
class Mercado:
    def __init__(self, nome_cliente, telefone_cliente, endereco_cliente):
        self._nome = nome_cliente
        self._telefone = telefone_cliente
        self._endereco = endereco_cliente
    
class Cliente(Mercado):
    def __init__(self, nome_cliente, telefone_cliente, endereco_cliente):
        super().__init__(nome_cliente, telefone_cliente, endereco_cliente)
    
    #Método para exibir informações do cliente
    def __str__(self):
        return f'Cliente: {self._nome}\nTelefone: {self._telefone}\nEndereço: {self._endereco}'
    
    #def relizar_compra(self, ):

class Produto:
    def __init__(self, nome_produto, quantidade_produtos):
        self.nome = nome_produto
        self.categoria = []
        self.quantiade = quantidade_produtos
        self.fornecedores =[]

cliente1 = Cliente("Clarice", 87879494, "Campina Grande")
print(cliente1)