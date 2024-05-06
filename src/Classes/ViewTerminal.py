from .BibliotecaController import BibliotecaController


class ViewTerminal:
    
    def __init__(self):
        self.biblioteca = BibliotecaController()


    def escrever(self, mensagem, indicador_inicio_mensagem='# '):
        print(f'\n\n{indicador_inicio_mensagem}{mensagem}')
        
        
    def imprimir_lista(self, menu: list):
        saida_menu = ''
        
        for indice, opcao in enumerate(menu):
            saida_menu += f'  [{indice+1}] {opcao}\n' 
        
        self.escrever(saida_menu, '')
        
        
    def perguntar(self, pergunta: str, menu: list = None):
        
        if not menu:
            self.escrever(pergunta)
            return input('\n\n > ')
            
        pergunta += ' (Digite o número da opção desejada)'
        
        self.escrever(pergunta)
        self.imprimir_lista(menu)
        return input('\n\n > ')


    def index(self):
        resposta_usuario = self.perguntar('Olá, o que deseja fazer hoje?', [
            'Listar todos os livros',
            'Adicionar um livro',
            'Consultar um livro',
            'Alocar um livro',
            'Renovar locação de um livro',
            'Listar livros alocados por um usuário',
            'Devolver um livro',
        ])
        
        self.rotear(int(resposta_usuario))
    
    def rotear(self, resposta_usuario):
        roteador = [
            self.listar_todos_titulos,
            self.adicionar_livro,
            self.consultar_livro,
            self.alocar_livro,
            self.renovar_locacao,
            self.listar_livros_alocados_usuario,
            self.devolver_livro,
        ]
        
        roteador[resposta_usuario]()


    def listar_todos_titulos(self):
        lista_titulos = self.biblioteca.listar_todos_titulos()

        self.imprimir_lista(lista_titulos)



    def adicionar_livro(self):
        titulo = self.perguntar("Qual o título do livro que deseja adicionar?")
        
        resultado = self.biblioteca.adicionar_livro(titulo)
        
        self.escrever(resultado)



    def consultar_livro(self):
        titulo = self.perguntar("Qual o titulo do livro que deseja consultar?")
        
        livro = self.biblioteca.consultar_livro(titulo)
        
        if livro:
            print(f"Nome do locador: {livro.locador}")
            print(f"Dias restantes para devolução: {livro.dias_devolucao}")
        else:
            print("Livro não encontrado.")


    def adicionar_livro(self):
        titulo = self.perguntar("Qual o título do livro que está adicionando?")
        locador = input("Digite o nome do locador: ")
        dias_devolucao = int(input("Digite a quantidade de dias para devolução: "))
        
        self.biblioteca.adicionar_livro(titulo, locador, dias_devolucao)
        
        print("Livro adicionado com sucesso!")

