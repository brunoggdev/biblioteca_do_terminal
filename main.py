import atexit
from src.Classes.ViewTerminal import ViewTerminal


view = ViewTerminal()

view.index()

def de_novo():
    if view.perguntar('Realizar outra operação? [s/n]') == 's':
        view.index()

atexit.register(de_novo)