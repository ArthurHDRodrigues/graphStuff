from graphClasses import *

import random

def genCaminho(graph, n, v):
    '''
    grafo,int,vertex->list

    recebe um grafo, um inteiro e um vértice do grafo e devolve um caminho com inicio em v de tamanho n
    '''

    if n<0:
        print("tamanho invalido")
        return None
    if v not in graph.vertexSet:
        print("vertice não esta no grafo")
        return None
    path = [v]
    vizitados = {v.id:graph.getNeighbor(v)}
    for i in range(1,n):
        if path[-1].id not in vizitados:
            vizitados[path[-1].id] = graph.getNeighbor(path[-1])
        l = len(vizitados[path[-1].id])
        r = random.randint(0,l-1)
        path.append(vizitados[path[-1].id][r])

    return path

def calcFrq(caminho, n):
    '''recebe um caminho e devolve um array com a frequencia normatizada de cada vértice'''
    freq = np.zeros(n)
    for v in caminho:
            freq[v.id]+=1
    for i in range(n):
            freq[i] = freq[i]/len(caminho)
    return freq

def calcFrqTeo(graph):
    freq = np.zeros(len(graph.vertexSet))

    m = len(graph.edgeSet)
    for v in graph.vertexSet:
        freq[v.id] = v.grau(graph.edgeSet)/(2*m)
    return freq
