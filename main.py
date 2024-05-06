import atexit
from src.Classes.ViewTerminal import ViewTerminal


view = ViewTerminal()

view.index()

def outra_operacao():
    if view.perguntar('Realizar outra operação? [s/n]') == 's':
        view.index()

atexit.register(outra_operacao)