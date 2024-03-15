from leitorarquivo import LeitorArquivo

if __name__ == '__main__':
    leitor = LeitorArquivo("data.txt")
    listaValores = leitor.getValores()
    print(listaValores)        