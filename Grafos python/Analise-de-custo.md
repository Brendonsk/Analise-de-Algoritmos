#Custo BFS

def BFS(Adj, s, tam):                           
    s=int(s)                                    # O(1)
    color = []                                  # O(1)
    d = []                                      # O(1)
    pi = []                                     # O(1)
    Q = []                                      # O(1)
    u = 0                                       # O(1)

    for u in range(tam):                        #
        if u != s:                              #
            color.append("w")                   #
            d.append(math.inf)                  #
            pi.append(None)                     #

    color.insert(s,"g")                         #
    d.insert(s,0)                               #
    pi.insert(s,None)                           #

    Q.insert(0,s)                               # O(1)

    while Q:                                    #
        u = Q[-1]                               #
        
        for v in range(tam):                    #
            if Adj[u][v] == 1:                  #
                if color[v] == 'w':             #
                    color[v] = 'g'              #
                    d[v] = d[u]+1               #
                    pi[v] = u                   #
                    Q.insert(0,v)               #
        Q.pop()                                 # O(1)
    color[u]='b'                                #
    print("\nd: "+str(d))                       #
    print("pi: "+str(pi))                       #
    print("c: "+str(color))                     #