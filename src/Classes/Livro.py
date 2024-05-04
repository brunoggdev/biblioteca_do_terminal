class Livro:
    '''Entity/DTO'''
    
    def __init__(self, titulo: str, locador: str = None, dias_para_devolucao: int = None):
        self.titulo = titulo
        self.locador = locador
        self.dias_para_devolucao = dias_para_devolucao



    def dicionario(self):
        '''Retorna as informações do livro em formato de dicionario'''
        
        return {
            'titulo': self.titulo, 
            'locador': self.locador, 
            'dias_para_devolucao': self.dias_para_devolucao
        }
