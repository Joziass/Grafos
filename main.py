# -*- coding: utf-8 -*-
from graph import Graph

def load_from(fileName):
    f = open(fileName, 'r')
    n = int(f.readline())
    
    g = Graph(n)
    
    l = 0
    for line in f:
        line.strip()
        numeros = line.split("\t")
        con = 0
        for i in numeros:
            if(con == g.num_vertices):
                break
            g.matrix[l][con] = int(i)
            if(g.matrix[l][con] > 0):
                g.list[l].append(con)
            
            con += 1
        l += 1
    return g

gr = load_from("pcv10.txt")
gr.print()
#dist, ant = gr.bfs(3)
#print(dist)
#print(ant)
gr.bfs_p(3,1)
print(gr.dfs())