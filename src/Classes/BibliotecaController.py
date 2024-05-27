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
            
        
    
    
    def renovar_locacao(self, id_livro: int|str, dias_adicionais: int):
        
        livro = self.model.buscar_por_id(int(id_livro))
        
        if not livro:
            return "Livro não identificado."
        
        livro.dias_para_devolucao += int(dias_adicionais)
        
        sucesso = self.model.salvar(livro)
        
        if not sucesso:
            return f"Falha ao renovar locação do livro '{livro.titulo}' para '{livro.locador}'..."
        
        return f"Locação do livro '{livro.titulo}' para '{livro.locador}' renovada com sucesso. O novo prazo é de {livro.dias_para_devolucao} dias."



    def consultar_livro(self, id_livro: int|str):
        
        livro = self.model.buscar_por_id(int(id_livro))
        
        if not livro:
            return "Livro não identificado."
        
        if livro.disponivel_para_locacao():
            return f"O livro '{livro.titulo}' está disponível para locação."

        return f"O livro '{livro.titulo}' está locado para '{livro.locador}'. Restam {livro.dias_para_devolucao} dias para devolução."



    def locar_livro(self, id_livro: int|str, locador: str, dias_locacao: int|str):
        livro = self.model.buscar_por_id(int(id_livro))
        
        if not livro:
            return "Livro não identificado."

        if not dias_locacao.isdigit():
            return f"Dias para locação deve ser um inteiro. Invés disso foi Foi recebido {dias_locacao}"
        
        livro.locador = locador
        livro.dias_para_devolucao = dias_locacao
        
        sucesso = self.model.salvar(livro)
        
        if not sucesso:
            return f"Houve um erro inesperado ao locar o livro..."
        
        return f"Livro '{livro.titulo}' locado com sucesso para '{locador}' por {dias_locacao} dias"



    def devolver_livro(self, id_livro: int|str, dias_locado: int|str):
        livro = self.model.buscar_por_id(int(id_livro))
        
        if not livro:
            return "Livro não identificado."
        
        if livro.disponivel_para_locacao():
            return f"O livro selecionado não parece estar locado."
        
        livro.dias_para_devolucao = 0
        sucesso = self.model.salvar(livro)
        
        if not sucesso:
            return f"Houve um problema com a devolução do livro..."
        
        atraso = int(dias_locado) - livro.dias_para_devolucao
        
        if atraso > 0:
            multa = atraso * self.multa_por_dia  # Exemplo de multa de R$0.50 por dia de atraso
            return f"Livro devolvido com atraso de {atraso} dias. Multa a ser paga: R${multa:.2f}."
        
        return f"Devolução do livro '{livro.titulo} finalizada."



    def listar_locacoes_usuario(self, locador: str):
        lista_livros = self.model.listar_por_locador(locador)

        if not lista_livros:
            return f"Nenhum livro encontrado para '{locador}'."
        
        return [livro.titulo for livro in lista_livros]