from sre_compile import isstring
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
            self.renovar_locacao,
            self.listar_locacoes_usuario,
            self.devolver_livro,
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
        id_livro = self.perguntar(
            "Qual dos livros deseja consultar?", 
            self.biblioteca.listar_todos_titulos()
        )
        
        consulta = self.biblioteca.consultar_livro(id_livro)
        
        self.escrever(consulta)
        


    def locar_livro(self):
        id_livro = self.perguntar(
            "Qual dos livros abaixo você deseja locar?", 
            self.biblioteca.listar_todos_titulos()
        )
        
        locador = self.perguntar("Qual o nome do locador?")
        dias_locacao = self.perguntar("Por quantos dias o livro será locado?")
        
        resposta = self.biblioteca.locar_livro(id_livro, locador, dias_locacao)
        
        self.escrever(resposta)



    def renovar_locacao(self):
        id_livro = self.perguntar(
            "Para qual dos livros abaixo você deseja renovar a locação?", 
            self.biblioteca.listar_todos_titulos()
        )
        
        dias_adicionais = self.perguntar("Quantos dias deseja adicionar ao periodo de locação?")
        
        resposta = self.biblioteca.renovar_locacao(id_livro, dias_adicionais)
        
        self.escrever(resposta)



    def devolver_livro(self):
        id_livro = self.perguntar(
            "Para qual dos livros abaixo você deseja devolver?", 
            self.biblioteca.listar_todos_titulos()
        )
        
        dias_locado = self.perguntar("Por quantos dias esse livro ficou locado? (deixe em branco para usar o prazo total de devolução)")
        
        resposta = self.biblioteca.devolver_livro(id_livro, dias_locado)
        
        self.escrever(resposta)
        
        
        
    def listar_locacoes_usuario(self):
        nome_usuario = self.perguntar('Digite o nome do usuário cujas locações deseja listar')
        
        resposta = self.biblioteca.listar_locacoes_usuario(nome_usuario)
        
        if isinstance(resposta, str):
            return self.escrever(resposta)
        
        self.imprimir_lista(resposta)
            

