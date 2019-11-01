import random
import math

def BFS(Adj, s, tam):
    """
    Busca em Largura(Breadth First Search)
    Procedimento que explora simetricamente os vértices de um grafo G(v,e)
    É chamada em largura porque explora todos os vértices diretamente conectados ao vértice fonte antes de explorar os vértices mais distantes

    Parameters:
        Adj (int[]): Matriz de adjacências de um determinado grafo G(v,e)
        s (int): Vértice fonte da busca, a partir do qual é executada a busca, começando por seus vértices adjacentes
        tam (int): Quantidade de vértices de um grafo G(v,e)
    """

    s=int(s)

    color = [] 
    d = [] 
    pi = [] 
    Q = [] 
    u = 0

    """
    Loop para a definição das posições iniciais dos vetor color,d e pi, com seus valores padrão
    """
    for u in range(tam):
        if u != s:
            color.append("w") 
            d.append(math.inf) 
            pi.append(None)

    """
    Inserções nos vetores color,d e pi, nas posição 's'
    """
    color.insert(s,"g") 
    d.insert(s,0)
    pi.insert(s,None)
    
    """
    Método de inserção num vetor
    Aqui, para utilizá-lo para inserir um elemento novo numa fila, o elemento é inserido na posição 0, e os demais elementos do vetor são movidos uma posição para a direita
    """
    Q.insert(0,s)

    while Q:
        """
        A variável "u" recebe a posição -1 da fila Q, ou seja, a última posição dela, também conhecida como cabeça
        """
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
    print("\nd: "+str(d))
    print("pi: "+str(pi))
    print("c: "+str(color))

G = []
vertices = int(input("Insira a quantidade de vértices do grafo: "))

manual = input("\nDeseja inserir sua matriz de adjacencias manualmente[S/N]?\nCaso contrario, sera gerada uma matriz M[vertices x vertices] aleatória\n\n")
if manual.upper()=="S":
    for i in range(vertices):
        G.append([])
        for j in range(vertices):
            entrada = int(input("G[{}][{}] = ".format(i,j)))
            G[i].append(entrada)
else:
    """
    Loop para atribuições aleatórias de 0 ou 1 na matriz de adjacências de um grafo
    """
    linha = "\nMatriz:\n\n"
    for i in range(vertices):
        linha += "|"
        G.append([])
        for j in range(vertices):
            G[i].append(random.randint(0,1))
            linha += str(G[i][j]) + "|"
        linha+="\n"
    
    #Impressão da matriz de adjacências para o usuario
    print(linha)

BFS(G,0,vertices)