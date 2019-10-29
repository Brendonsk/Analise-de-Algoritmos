import random

def BFS(Adj, s, tam):
    color = [] 
    d = [] 
    pi = [] 
    Q = [] 
    u = 0 
    for u in range(tam):
        if u != s:
            color.append('w') 
            d.append("infinito") 
            pi.append('/')

    color.insert(s,'g') 
    d.insert(s,0)
    pi.insert(s,'/')

    Q.insert(0,s)

    while Q:
        u = Q[-1] 
        for v in range(tam):
            if Adj[u][v] == 1:
                if color[v] == 'w':
                    color[v] = 'g' 
                    d[v] = d[u]+1 
                    pi[v] = u 
                    Q.insert(0,v)
    Q.pop() 
    color[u]='b'
    print("d: "+str(d))
    print("pi: "+str(pi))
    print("c: "+str(color))

G = []
vertices = int(input("Insira a quantidade de vértices do grafo: "))

linha = ""
for i in range(vertices):
    linha += "|"
    G.append([])
    for j in range(vertices):
        G[i].append(random.randint(0,1))
        linha += str(G[i][j]) + "|"
    linha+="\n"
print(linha)
BFS(G,0,6)