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
        
        self.escrever(pergunta)
        if menu:
            self.imprimir_lista(menu)

        resposta = input('\n\n > ')
        
        if resposta == 'sair':
            exit()
        
        return resposta


    def index(self):
        resposta_usuario = self.perguntar(
            'Olá, o que deseja fazer hoje? (Digite o número da opção desejada ou sair para finalizar)', 
            [
                'Listar todos os livros',
                'Adicionar um livro',
                'Consultar um livro',
                'Locar um livro',
                'Renovar locação de um livro',
                'Listar livros locados por um usuário',
                'Devolver um livro',
            ]
        )
        
        self.rotear(int(resposta_usuario))
    
    
    
    def rotear(self, resposta_usuario):
        roteador = [
            self.listar_todos_titulos,
            self.adicionar_livro,
            self.consultar_livro,
            self.locar_livro,
            # self.renovar_locacao,
            # self.listar_livros_alocados_usuario,
            # self.devolver_livro,
        ]
        
        roteador[resposta_usuario-1]()


    def listar_todos_titulos(self):
        lista = self.biblioteca.listar_todos_titulos()
        self.imprimir_lista(lista)



    def adicionar_livro(self):
        titulo = self.perguntar("Qual o título do livro que deseja adicionar?")
        
        resposta = self.biblioteca.adicionar_livro(titulo)
        
        self.escrever(resposta)
        
        
    def consultar_livro(self):
        id_livro = self.perguntar('Qual dos livros deseja consultar?', self.biblioteca.listar_todos_titulos())
        
        consulta = self.biblioteca.consultar_livro(id_livro)
        
        self.escrever(consulta)
        
        




    def locar_livro(self):
        id_livro = self.perguntar("Qual dos livros abaixo você deseja locar?", self.biblioteca.listar_todos_titulos())
        locador = self.perguntar("Qual o nome do locador?")
        dias_locacao = self.perguntar("Por quantos dias o livro será locado?")
        
        resposta = self.biblioteca.locar_livro(id_livro, locador, dias_locacao)
        
        self.escrever(resposta)


    # def adicionar_livro(self):
    #     titulo = self.perguntar("Qual o título do livro que está adicionando?")
    #     locador = input("Digite o nome do locador: ")
    #     dias_devolucao = int(input("Digite a quantidade de dias para devolução: "))
        
    #     self.biblioteca.adicionar_livro(titulo, locador, dias_devolucao)
        
    #     print("Livro adicionado com sucesso!")

