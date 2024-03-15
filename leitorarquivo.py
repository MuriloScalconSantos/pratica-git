class LeitorArquivo:
    def __init__(self, nomeArquivo):
        self.arq = open(nomeArquivo, 'r')
        self.valores = [float(x) for x in self.arq.readline().split()]
   
    def getValores(self):
        return self.valores


if __name__ == '__main__':
    leitor = LeitorArquivo("data.txt")
    listaValores = leitor.getValores()
    print(listaValores)        