# -*- coding: utf-8 -*-
import queue

class Graph:
    def __init__(self, n):
        self.num_vertices = n
        self.matrix = [[0 for _ in range(n)] for _ in range(n)]
        self.list = [[] for _ in range(n)]
        

    def print(self):
        print(self.matrix)
        print(self.list)
        
    
                    
    def dfs(self):
        ant = [-1 for _ in range(self.num_vertices)]
        isVisited = [False for _ in range(self.num_vertices)]
        
        for i in range(self.num_vertices):
            if (isVisited[i]==False):
                isVisited[i]=True
                falta_visitar = [i]
                while falta_visitar:
                    vertice = falta_visitar.pop()
                    for vizinho in self.list[vertice]:
                        if (isVisited[vizinho]==False):
                            ant[vizinho] = vertice
                            isVisited[vizinho]=True
                            falta_visitar.append(vizinho)
        
        return ant
        
    def bfs(self, source):
        dist = [-1 for _ in range(self.num_vertices)]
        ant = [-1 for _ in range(self.num_vertices)]
        isVisited = [False for _ in range(self.num_vertices)]
        Q = queue.Queue()
        Q.put(source)
        isVisited[source] = True
        dist[source] = 0
        
        while Q.empty() != True:
            p = Q.get()
            
            for v in self.list[p]:
                if isVisited[v] == False:
                    dist[v] = dist[p] + 1
                    ant[v] = p
                    Q.put(v)
                    isVisited[v] = True
        
        return dist, ant
    
    def bfs_p(self, source, destino):
        dist, ant = self.bfs(source)
        if (dist[destino]==-1):
            print("não há caminho entre os vértices")
            
        else:
            caminho=[]
            caminho.append(destino)
            c=ant[destino]
            for _ in range(dist[destino]):
                caminho.append(c)
                c=ant[c]
            print(caminho)