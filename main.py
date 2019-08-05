import sys, pygame

from graphClasses import *
from genGraphs  import *
from randomWalk import *


def formatFile(fileName):
    '''
    recebe um nome de arquivo, abre e formata em uma lista onde as seus elementos são:
    [tipo do elemento, elemento]
    '''
    f = open(fileName,"r")
    fl = f.readlines()
    types = ['undirected','directed','mixed']
    formatedFile = []

    for line in fl:
            #Formata cada linha em uma lista
            words = line.split(' ')
            words[-1] = words[-1].split('\n')[0]
            #print(words)

            formatedFile.append(words)
            f.close
    return formatedFile

def genGraph(formatedFile):
    #recebe um arquivo formatado e devolve um grafo
    types = ['undirected','directed','mixed']

    if formatedFile[0][0] not in types:
        print("Tipo de grafo não listado")
        return None
    else:
        type = formatedFile[0][0]
        n = int(formatedFile[1][0])

        vertexList = []
        for i in range(n):
            vertexList.append(vertex(i))

        edgeList = []
        formatedFile.pop(0) #tira o tipo do grafo
        formatedFile.pop(0) #tira o número de vértices do grafo
        for i in formatedFile:
            if i[0] == 'edge':
                e = i[1].split(',')
                edgeList.append(edge(vertex(e[0]),vertex(e[1])))
            elif i[0]!= '':
                print("Tipo não listado")
    graph = Graph(type,vertexList,edgeList)
    return graph

def main():
    #print("lendo arquivo\n")
    fileName = str(sys.argv[1])

    formatedFile = formatFile(fileName)
    #print("arquivo lido e formatado\ngerando grafo")

    display = pygame.display.set_mode((1000,1000))

    #result = genGraph(formatedFile)
    result = genC(10)

    #result = genP(3) #graph.union(genC(5)).union(genP(5))
    #result.addEdge(edge(vertex(0),vertex(15)))
    #result.addEdge(edge(vertex(5),vertex(12)))

    print("\n\n Grafo final:")
    print(result.genRep(2))
    #L = result.genL()
    #print(L)
    #print("autovetores\n")
    #s,v = np.linalg.eig(L)
    #print(s[0].round(decimals=3))

    #print(v.round(decimals=3))
    #print("\nAdjacencia:\n")
    #print(graph.genA())
    #print("\nLaplaciana:\n")
    #print(graph.genL())
    #print("\nMatriz de distribuição de probabilidade:\n")
    #print(graph.genM())
    #print("\nAlgum caminho aleatório com 10 passos:\n")
    #caminho = genCaminho(result,1000,vertex(7))
    #print(caminho)
    #print("Frequência empirica:\n")
    #print(calcFrq(caminho,len(result.vertexSet)))

    #print("Frequencia teorica:\n")
    #print(calcFrqTeo(result))
    #print("\ngrafo completo K_n 10 vértices\n")
    #print(genK(10))
    #print("\ngrafo caminho P_n  com 10 vértices\n")
    #print(genP(10))
    #print("\nCiclo C_n  com 10 vértices\n")
    #print(genC(10))
    display.fill((255,255,255))
    result.draw(display)
    pygame.display.flip()
    input("Sair?")

if __name__ == "__main__":
        main()
