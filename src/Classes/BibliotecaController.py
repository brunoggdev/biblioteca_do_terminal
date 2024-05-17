from .Livro import Livro
from .LivroModel import LivroModel


class BibliotecaController:

    def __init__(self):
        self.multa_por_dia = 0.5
        self.model = LivroModel()


    def listar_todos_titulos(self):
        lista_livros = self.model.listar_todos()
        
        return [livro.titulo for livro in lista_livros]
    
    
    def adicionar_livro(self,  titulo: str):
        livro = Livro(titulo)
        
        sucesso = self.model.salvar(livro)
        
        if not sucesso:
            return f"Livro '{titulo}' não pôde ser adicionado..."
        
        return f"Livro '{titulo}' adicionado com sucesso!"
            
        
    
    
    
    def renovar_locacao(self, titulo: str, dias_adicionais: int):
        livro = self.model.buscar_por_titulo(titulo)
        
        livro.dias_para_devolucao += dias_adicionais
        
        self.model.salvar(livro)
        
        return f""



    def consultar_livro(self, id_livro: int|str):
        
        livro = self.model.buscar_por_id(int(id_livro))
        
        if livro.disponivel_para_locacao():
            return f"O livro '{livro.titulo}' está locado para '{livro.locador}'. Restam {livro.dias_para_devolucao} dias para devolução."
        else:
            return f"O livro '{livro.titulo}' está disponível para locação."



    def locar_livro(self, id_livro: int|str, locador: str, dias_locacao: int|str):
        livro = self.model.buscar_por_id(int(id_livro))

        if not livro.disponivel_para_locacao():
            return f"O livro '{livro.titulo}' não está disponível para locação."
        
        if not dias_locacao.isdigit():
            return f"Dias para locação deve ser um inteiro. Invés disso foi Foi recebido {dias_locacao}"
        
        livro.locador = locador
        livro.dias_para_devolucao = dias_locacao
        
        sucesso = self.model.salvar(livro)
        
        if not sucesso:
            return f"Houve um erro inesperado ao locar o livro..."
        
        return f"Livro '{livro.titulo}' locado com sucesso para '{locador}'"



    def devolver_livro(self, dias_locado: int):
        atraso = dias_locado - self.dias_para_devolucao
        if atraso > 0:
            multa = atraso * 0.5  # Exemplo de multa de R$0.50 por dia de atraso
            return f"Você ultrapassou o prazo de devolução em {atraso} dias. Multa a ser paga: R${multa:.2f}"
        else:
            return "Livro devolvido com sucesso."
