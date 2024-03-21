from leitorarquivo import LeitorArquivo
import numpy as np
import matplotlib.pyplot as plt

def main():

    leitor = LeitorArquivo("data.txt")
    listaValores = leitor.getValores()
    print(listaValores)     
    
    #Plotando gráfico de linhas
    plt.subplot(1, 2, 1)
    plt.ylabel('Valores de entrada')
    plt.xlabel('Amostragem')
    plt.xlabel('Gráfico de linhas')
    
    i = 1
    for serie in listaValores:
        plt.plot(serie, label='Série ' + str(i))   
        i += 1
    plt.legend(loc='upper left')
    #Plotando gráfico de barras (médias)
    plt.subplot(1, 2, 2)
   
    medias = leitor.getMedias()
    xvalues = np.arange(1, len(medias)+1)
    plt.bar(xvalues, medias)  
    plt.xticks(xvalues, ['Série ' + str(x) for x in xvalues])
    plt.title('Médias das séries')
    plt.ylabel('Valores de entrada')
    plt.xlabel('Amostragem')

    plt.show()

main()