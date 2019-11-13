import numpy as np

class vertex:
    def __init__(self, id = 0, pos = [100,100]):
        #id é necessariamente um inteiro
        self.id = int(id)
        self.pos = pos

    def __str__(self):
        return "vertice: "+str(self.id)
    def __repr__(self):
        return str(self.id)

    def __eq__(self,other):
        return self.id == other.id

    def grau(self, edgeList):
        n=0
        for i in edgeList:
            if self in i.comp:
                n+=1
        return n

    def draw(self,surf):
        pygame.draw.circle(surf,(0,0,0,255),self.pos,5)


class edge:
    def __init__(self,x,y):
        self.comp = [x,y]
        self.x = x
        self.y = y
    def __str__(self):
        return "( "+ str(self.x.id)+" , "+str(self.y.id)+" )"

    def draw(self,surf):
        pygame.draw.line(surf,(0,255,0,255),self.x.pos,self.y.pos,2)


class Graph:
    def __init__(self,type,vertexList,edgeList,flag=''):
        self.type = type
        self.vertexSet = vertexList

        if flag == 'f':
            self.edgeSet = edgeList
        else:
            self.edgeSet = []
            for e in edgeList:
                self.addEdge(e)

    def __str__(self):
        r = "tipo: " + self.type + "\n"
        r += "vértices:\n ["
        for v in range(len(self.vertexSet)-1):
            r+=str(self.vertexSet[v].id)+", "
        r+=str(self.vertexSet[-1].id)+"]\n"
        r+="Arestas:\n"
        c = 0
        for e in self.edgeSet:
            r+=str(e)+" "
            if c < 10:
                c+=1
            else:
                c=0
                r+="\n"
        return r


    def addVertex(self, inputV):
        #adiciona um vertex inputV no conjunto V
        self.vertexSet.append(vertex(inputV))

    def addEdge(self, e):
        # recebe um objeto da classe edge e
        # verifica se e.x e e.y estão em V e depois add e em E
        if e.x not in self.vertexSet:
            print("vertice", e.x,"da aresta", e , "não está no conjunto de vertices")

        else:
            if e.y not in self.vertexSet:
                print("vertice", e.y,"da aresta", e , "não está no conjunto de vertices")

            else:
                self.edgeSet.append(e)

    def getNeighbor(self, v):
        '''
        vertex->list
        recebe um vértice e devolve a lista de vizinhos deste vértice
        '''
        vizinhos =[]
        for e in self.edgeSet:
            if v in e.comp:
                if v == e.x:
                    vizinhos.append(e.y)
                else:
                    vizinhos.append(e.x)
        return vizinhos

    def draw(self,surf):
        for e in self.edgeSet:
            e.draw(surf)
        for v in self.vertexSet:
            v.draw(surf)

    def genA(self):
        #gera a matriz de adjacencia A
        l = len(self.vertexSet)
        matrixA = np.zeros([l,l], dtype=int)

        if self.type == 'directed':
            for e in self.edgeSet:

                matrixA[e.x.id][e.y.id] = 1

        elif self.type == 'undirected' or self.type == 'mixed':
            for e in self.edgeSet:
                matrixA[e.x.id][e.y.id] += 1
                matrixA[e.y.id][e.x.id] += 1
        return matrixA
    def genQ(self):
        #gera a matriz de incidência VxE
        n = len(self.vertexSet)
        m = len(self.edgeSet)
        Q = np.zeros([n,m], dtype=int)

        for i in range(m):
            Q[self.edgeSet[i].x.id][i] = 1
            Q[self.edgeSet[i].y.id][i] = 1

        return Q


    def genD(self):
        #gera a matriz diagonal com os grais dos vértices
        n = len(self.vertexSet)
        matrixD = np.zeros([n,n], dtype=int)

        for e in self.edgeSet:
            matrixD[e.x.id][e.x.id]+=1
            matrixD[e.y.id][e.y.id]+=1

        return matrixD

    def genDedge(self):
        #gera a matriz diagonal com os grais das arestas
        m = len(self.edgeSet)
        matrixD = np.zeros([m,m], dtype=int)

        for i in range(m):
            if(self.edgeSet[i].x.id == self.edgeSet[i].y.id):
                matrixD[i][i] = 1
            else:
                matrixD[i][i] = 2
            
        return matrixD



    def genL(self):
        #L := D-A
        D = self.genD()
        A = self.genA()

        #L = -1*self.genA()
        #l = len(self.vertexSet)
        #for i in range(l):
        #    L[i][i] = L[i].sum()*-1

        return D-A


    def genM(self):
        #gera a matriz de distribuição de probabilidade
        M = self.genA().astype(float)
        l = len(self.vertexSet)
        for i in range(l):
            s = M[i].sum()
            M[i] = M[i]/s
        return M

    def genLoop(self):
        D = self.genD()


    def genRep(self,n):
        #gera uma matriz de representação de G de n-ésima dimensão.
        L = self.genL()
        s,v = np.linalg.eig(L)#.round(decimals=3)
        s = s.round(decimals=3)
        v = v.round(decimals=3)
        w  = np.transpose(v)
        o = np.argsort(s)
        #s[o[0]] = 0
        #v[o[0]] = (1,1,1,...,1)
        r = []
        for i in range(n):
            r.append(w[o[i+1]])
        r = np.array(r)
        if(n==2):
            c = r*100+500
            c = c.astype(int)
            for v in self.vertexSet:
                v.pos = [c[0][v.id],c[1][v.id]]
            for e in self.edgeSet:
                e.x.pos = [c[0][e.x.id],c[1][e.x.id]]
                e.y.pos = [c[0][e.y.id],c[1][e.y.id]]
        return np.transpose(r)

    def genNewL(self):
        D = self.genD()
        edgeD = np.linalg.inv(self.genDedge())
        Q = self.genQ()

        QD = Q.dot(edgeD)
        QT = np.transpose(Q)
        newL = D - QD.dot(QT)
        return newL

    def union(self,other):
        '''
        recebe dois grafos e devolve a união deles
        '''

        if len(self.edgeSet)<len(other.edgeSet):
            menor = self
            maior = other
        else:
            menor = other
            maior = self

        graph = maior
        n = len(menor.vertexSet)
        m = len(maior.vertexSet)

        vertexList = maior.vertexSet

        for i in range(n):
            vertexList.append(vertex(m+i))

        edgeList = maior.edgeSet

        for e in menor.edgeSet:
                edgeList.append(edge(vertex(e.x.id+m),vertex(e.y.id+m)))
        return Graph('undirected',vertexList,edgeList,'f')
