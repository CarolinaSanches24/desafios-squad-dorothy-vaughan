import colorama;
colorama.init();

# encapsulamento 
class Usuario:
    def __init__(self, nome, telefone, nacionalidade):
        self.__nome = nome
        self.__telefone = telefone
        self.__nacionalidade = nacionalidade

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
            
    @property
    def telefone(self):
        return self.__telefone
    
    @telefone.setter
    def telefone(self, novo_telefone):
        self.__telefone = novo_telefone
    
    @property
    def nacionalidade(self):
        return self.__nacionalidade
    
    @nacionalidade.setter
    def nacionalidade(self, nova_nacionalidade):
        self.__nacionalidade = nova_nacionalidade
        
        # método para mostrar as informações do usuário
    def __str__(self):
        return (
        f'Nome: {self.__nome}\n' +
        f'Telefone: {self.__telefone}\n'+
        f'nacionalidade:{self.__nacionalidade}'
    )
class Livro:
    def __init__(self, titulo, editora, numero_maximo_renovacoes):
        self.titulo = titulo
        self.editora = editora
        self.generos = [];
        self.numero_maximo_renovacoes = numero_maximo_renovacoes
        self.autores = []
        self.exemplares = []


    def adicionar_autor(self, autor):
        self.autores.append(autor)

    def adicionar_exemplar(self, exemplar):
        self.exemplares.append(exemplar)
        
    def adicionar_genero(self, genero):
        self.generos.append(genero);
        
    def __str__(self):
       return (
        colorama.Fore.MAGENTA + '[Info Livro]' + colorama.Style.RESET_ALL +
        f'\nTítulo: {self.titulo}\n' +
        f'Editora: {self.editora}\n' +
        f'Número Máximo de Renovações Permitidas: {self.numero_maximo_renovacoes}\n' +
        f'Autores: {self.autores}\n' +
        f'Gêneros: {self.generos}\n' +
        f'Exemplares Disponiveis: {len(self.exemplares)}'
    )
       
class Exemplar:
    def __init__(self, livro):
        self.livro = livro
        self.estado = "disponivel"
        self.data_emprestimo = None
        self.data_devolucao = None
        self.renovacoes = 0



usuario = Usuario(" Juliana", "84237428", "Brasileiro")
print(usuario);


livro = Livro("Harry Potter", "Editora A", 5)
livro.adicionar_autor('JK Rolling')
livro.adicionar_genero('Ficçao')
livro.adicionar_exemplar(livro.titulo);
livro.adicionar_exemplar(livro.titulo);
print(livro)
print(livro.exemplares)
    
exemplar = Exemplar(livro);
print(exemplar.livro)

   