from src.Classes.ViewTerminal import ViewTerminal


def main():
    view = ViewTerminal()

    while True:
        view.index()

        if view.perguntar('Realizar outra operação? [s/n]') != 's':
            break

if __name__ == "__main__":
    main()