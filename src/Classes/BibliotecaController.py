from .Livro import Livro
from .LivroModel import LivroModel


class BibliotecaController:

    def __init__(self ):
        self.multa_por_dia = 0.5
        self.model = LivroModel()


    def listar_todos_livros(self):
        return self.model.listar_todos()

    def adicionar_livro(self,  titulo: str):
        # TODO: validação
        livro = Livro(titulo)
        
        self.model.salvar(livro)
        
        return f"Livro '{titulo}' adicionado com sucesso!"
    
    
    
    def renovar_locacao(self, titulo: str, dias_adicionais: int):
        # TODO: validação
        livro = self.model.buscar_por_titulo(titulo)
        
        livro.dias_para_devolucao += dias_adicionais
        
        self.model.salvar(livro)
        
        return f""



    def consultar_locacao(self):
        if self.dias_para_devolucao > 0:
            return f"O livro '{self.titulo}' está locado para '{self.locador}'. Restam {self.dias_para_devolucao} dias para devolução."
        else:
            return f"O livro '{self.titulo}' não está locado."



    def devolver_livro(self, dias_locado: int):
        atraso = dias_locado - self.dias_para_devolucao
        if atraso > 0:
            multa = atraso * 0.5  # Exemplo de multa de R$0.50 por dia de atraso
            return f"Você ultrapassou o prazo de devolução em {atraso} dias. Multa a ser paga: R${multa:.2f}"
        else:
            return "Livro devolvido com sucesso."
