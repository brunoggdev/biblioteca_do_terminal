from .BibliotecaController import BibliotecaController


class ViewTerminal:
    
    def __init__(self):
        self.biblioteca = BibliotecaController()


    def escrever(self, mensagem, indicador_inicio_mensagem='# '):
        print(f'\n\n{indicador_inicio_mensagem}{mensagem}')
        
        
    def perguntar(self, pergunta: str, menu: dict = None):
        
        if not menu:
            self.escrever(pergunta)
            return input('\n\n > ')
            
        pergunta += ' (Digite o número da opção desejada)'
        
        saida_menu = ''
        for indice, opcao in menu.items():
            saida_menu += f'  [{indice}] {opcao}\n' 
        FAZER FUNçÃO DE IMPRIMIR LISTAGENS E USAR ARRAYS COM ENUMERATE INVÉS DE DICIONARIOS
        self.escrever(pergunta)
        self.escrever(saida_menu, '')
        return input('\n\n > ')


    def index(self):
        resposta_usuario = self.perguntar('Olá, o que deseja fazer hoje?', {
            1: 'Listar todos os livros',
            2: 'Adicionar um livro',
            3: 'Consultar um livro',
            4: 'Alocar um livro',
            5: 'Renovar locação de um livro',
            6: 'Listar livros alocados por um usuário',
            7: 'Devolver um livro',
        })
        
        self.rotear(resposta_usuario)
    
    def rotear(self, resposta_usuario):
        roteador = {
            1: self.listar_todos_livros,
            2: self.adicionar_livro,
            3: self.consultar_livro,
            4: self.alocar_livro,
            5: self.renovar_locacao,
            6: self.listar_livros_alocados_usuario,
            7: self.devolver_livro,
        }
        
        roteador[resposta_usuario]()


    def listar_todos_livros(self):
        lista = self.biblioteca.listar_todos_livros()

    def adicionar_livro(self):
        titulo = input("Digite o título do livro: ")
        locador = input("Digite o nome do locador: ")
        dias_devolucao = int(input("Digite a quantidade de dias para devolução: "))
        
        self.biblioteca.adicionar_livro(titulo, locador, dias_devolucao)
        
        print("Livro adicionado com sucesso!")



    def consultar_livro(self):
        titulo = input("Digite o título do livro a ser consultado: ")
        
        livro = self.biblioteca.consultar_livro(titulo)
        
        if livro:
            print(f"Nome do locador: {livro.locador}")
            print(f"Dias restantes para devolução: {livro.dias_devolucao}")
        else:
            print("Livro não encontrado.")


