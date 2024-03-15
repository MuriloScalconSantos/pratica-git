from leitorarquivo import LeitorArquivo
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    leitor = LeitorArquivo("data.txt")
    listaValores = leitor.getValores()
    print(listaValores)     
    
    plt.title('Gráfico de linhas')
    plt.ylabel('Valores de entrada')
    plt.xlabel('Amostragem')
    
    plt.plot(listaValores)
    plt.show()
