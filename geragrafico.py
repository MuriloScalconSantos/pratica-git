from leitorarquivo import LeitorArquivo
import numpy as np
import matplotlib.pyplot as plt

def main():

    leitor = LeitorArquivo("data.txt")
    listaValores = leitor.getValores()
    print(listaValores)     
    
    plt.ylabel('Valores de entrada')
    plt.xlabel('Amostragem')
    
    i = 1
    for serie in listaValores:
        plt.plot(serie, label='Série ' + str(i))   
        i += 1
    plt.legend(loc='upper left')
    plt.show()
    
main()