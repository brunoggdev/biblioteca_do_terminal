import csv
import os
from src.Classes.Livro import Livro

class LivroModel:
    '''Repository Pattern / DAO'''
    
    def __init__(self):
        self.tabela = os.path.join(os.path.dirname(__file__), '../tabela.csv')
    
    
    
    def __ler_tabela(self):
        with open(self.tabela, mode='r') as arquivo_csv:
            return list(csv.DictReader(arquivo_csv))



    def __atualizar_tabela(self, nova_tabela):
        with open(self.tabela, mode='w', newline='') as arquivo_csv:
            writer = csv.DictWriter(arquivo_csv, fieldnames=nova_tabela[0].keys())
            writer.writeheader()
            writer.writerows(nova_tabela)

    
    
    def buscar_por_id(self, id: str):
        tabela = self.__ler_tabela()
        
        for index, linha in enumerate(tabela):
            if index+1 == id:
                return Livro(**linha) #unpack
        
        return None
    
    
    
    def buscar_por_titulo(self, titulo: str):
        tabela = self.__ler_tabela()
        
        for linha in tabela:
            if linha['titulo'] == titulo:
                return Livro(**linha) #unpack
        
        return None



    def listar_todos(self) -> list[Livro]:
        tabela = self.__ler_tabela()
        
        lista = []
        
        for linha in tabela:
            lista.append(Livro(**linha)) #unpack
        
        return lista



    def listar_por_locador(self, locador: str) -> list[Livro]:
        tabela = self.__ler_tabela()
        
        lista = []
        
        for linha in tabela:
            if linha['titulo'] == locador:
                return Livro(**linha) #unpack
        
        return lista
    
    
    
    def salvar(self, livro: Livro):
        '''Cria ou atualiza um registro na tabela'''
        
        dados = livro.dicionario()
        tabela = self.__ler_tabela()
        livro_existe = self.buscar_por_titulo(dados['titulo'])

        if livro_existe:
            # Atualizar livro existente
            for linha in tabela:
                if linha['titulo'] == dados['titulo']:
                    linha.update(dados)
                    break
        else:
            # Adicionar novo livro
            tabela.append(dados)
        
        self.__atualizar_tabela(tabela)
        
        return True
