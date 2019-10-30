#Análise de custo BFS

- Análise do pior caso

<p>
def BFS(Adj, s, tam):                           
    s=int(s)                                    \# O(1)
    color = []                                  \# O(1)
    d = []                                      \# O(1)
    pi = []                                     \# O(1)
    Q = []                                      \# O(1)
    u = 0                                       \# O(1)

    for u in range(tam):                        \# v + 1 = O(v)
        if u != s:                              \# v = O(v)
            color.append("w")                   \# v - 1 = O(v)
            d.append(math.inf)                  \# v - 1 = O(v)
            pi.append(None)                     \# v - 1 = O(v)

    color.insert(s,"g")                         \# O(1)
    d.insert(s,0)                               \# O(1)
    pi.insert(s,None)                           \# O(1)

    Q.insert(0,s)                               \# O(1)

    while Q:                                    \# O(v)
        u = Q[-1]                               \# O(v)
        
        for v in range(tam):                    \# O(v²)
            if Adj[u][v] == 1:                  \# if(27-32): O(v²)
                if color[v] == 'w':             
                    color[v] = 'g'              
                    d[v] = d[u]+1               
                    pi[v] = u                   
                    Q.insert(0,v)               \# O(v²)
        Q.pop()                                 \# O(v)
    color[u]='b'                                \# O(1)
    print("\nd: "+str(d))                       \# O(v)
    print("pi: "+str(pi))                       \# O(v)
    print("c: "+str(color))                     \# O(v)

Dado um grafo G(v,e) qualquer:

O loop das linhas 11-15 atribui valores aos vetores "color", "d" e "pi" para as posições cujos índices representam os vértices do grafo que não são iguais ao vértice de origem s, possuindo custo total de 4v-2 e,  portanto, possui complexidade O(v)

O while das linhas 23 a 33 refere-se ao enfileiramento dos vértices do grafo cujo índice, no vetor color, são representados por 'w'(white), seguindo uma exploração em largura. Portanto, o pior caso ocorre quando o vértice origem está conectado a apenas um outro vértice, que por sua vez está conectado ao vértice de origem e a outro vértice, diferente dos vértices anteriores, seguindo um padrão de vértices conectados a dois outros vértices, até que o último vértice, que será conectado a apenas o vértice o qual já foi explorado, for explorado. Neste caso, a complexidade do while é igual a O(v).

O for das lnhas 26 a 32 possui complexidade fixa de O(v²), pois ele sempre fará v iterações, sendo (v-1) para o meio do loop, e v para o início dele, e ele está dentro do loop while, de complexidade O(v).

Com isso, é possível concluir que a complexidade do algoritmo BFS em seu pior caso é 

Referência Bibliográfica: CORMEN, Thomas H.; LEISERSON, Charles E.; RIVEST, Ronald L.
Introduction to algorithms. New York: Mcgraw-hill book, 1990. 1028 p. ISBN
0262530910.
