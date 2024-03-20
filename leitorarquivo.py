class LeitorArquivo:
    def __init__(self, nomeArquivo):
        self.arq = open(nomeArquivo, 'r')
        self.__leValores()


    def __leValores(self):
        self.valores = []
        for linha in self.arq.readlines():
            serie = [float(x) for x in linha.split()]
            self.valores.append(serie)

   
    def getValores(self):
        return self.valores