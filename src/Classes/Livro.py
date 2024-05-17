class Livro:
    '''Entity/DTO'''
    
    def __init__(self, titulo: str, locador: str = None, dias_para_devolucao: int = None):
        self.titulo = titulo
        self.locador = locador
        self.dias_para_devolucao = int(dias_para_devolucao) if dias_para_devolucao else 0


    def disponivel_para_locacao(self):
        return not self.dias_para_devolucao > 0
    

    def dicionario(self):
        '''Retorna as informações do livro em formato de dicionario'''
        
        return {
            'titulo': self.titulo, 
            'locador': self.locador, 
            'dias_para_devolucao': self.dias_para_devolucao
        }
