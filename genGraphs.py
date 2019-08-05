from graphClasses import *

def genK(n):

    '''
    int -> list
    recebe um inteiro positivo n e devolve uma lista da forma:
    [um grafo completo de n vértices,matriz de adjcencia,laplacina]
    '''
    vList = []
    eList = []
    for i in range(n):
        vList.append(vertex(i))

    for i in range(n):
        for j in range(i+1,n):
            eList.append(edge(vList[i],vList[j]))

    K = Graph('undirected',vList,eList,'f')

    return K

def genP(n):
        '''
        int -> list
        recebe um inteiro positivo n e devolve uma lista da forma:
        [um grafo completo de n vértices,matriz de adjcencia,laplacina]
        '''
        vList = []
        eList = []
        for i in range(n):
                vList.append(vertex(i,[10,i*20+5]))

        for i in range(n-1):
                eList.append(edge(vList[i],vList[i+1]))

        K = Graph('undirected',vList,eList,'f')

        return K

def genC(n):
    C = genP(n)
    C.addEdge(edge(vertex(n-1),vertex(0)))
    return C
