import random #biblioteca importada para a utilização da função random.randint(), para gerar uma matriz de adjacências aleatória

#inicialização dos arrays e inteiros para que possam ser utilizados dentro das funções como variáveis globais
G = []
color = []
d = []
pi = []
f = []
time = 0
tam = 0

"""
Busca em Profundidade(Depth First Search)
Procedimento que explora todos os vértices de um grafo G(v,e).
Nele, todas as arestas do vértice mais recentemente descoberto "v" são exploradas e,
quando não restam mais arestas inexploradas, a busca "regressa", explorando as arestas
que deixam o vértice a partir do qual "v" foi descoberto
"""
def DFS():
  global tam, G, color, d, f, pi, time
  
  for u in range(tam):
    color.append('w')
    d.append(0)
    f.append(0)
    pi.append(None)
  time = 0

  for u in range(tam):
    if color[u] == 'w':
      DFS_visita(u)

"""
Procedimento que explora recursivamente as arestas dum vértice U, que ainda não foram exploradas
"""
def DFS_visita(U):
  global tam, G, color, d, pi, time

  color[U] = 'g'
  time += 1
  d[U] = time

  for v in range(tam):
    if(G[U][v]==1 and color[v]=='w'):
      pi[v] = U
      DFS_visita(v)

  color[U] = 'b'
  time += 1
  f[U] = time

# Algoritmo visto em aula, utilizado aqui para debugar o código, e comentado para que não afete o mesmo
#
# tam = 6
# G = [
#     [0,1,0,1,0,0],
#     [0,0,0,0,1,0],
#     [0,0,0,0,1,1],
#     [0,1,0,0,0,0],
#     [0,0,0,1,0,0],
#     [0,0,0,0,0,1],
#     ]

#MAIN
tam = int(input("Insira a quantidade de vértices do grafo: "))

manual = input("\nDeseja inserir sua matriz de adjacencias manualmente[S/N]?\nCaso contrario, sera gerada uma matriz M[tam x tam] aleatória\n\n")
if manual.upper()=="S":
    for i in range(tam):
        G.append([])
        for j in range(tam):
            entrada = int(input("G[{}][{}] = ".format(i,j)))
            G[i].append(entrada)
else:
    """
    Loop para atribuições aleatórias de 0 ou 1 na matriz de adjacências de um grafo
    """
    linha = "\nMatriz:\n\n"
    for i in range(tam):
        linha += "|"
        G.append([])
        for j in range(tam):
            G[i].append(random.randint(0,1))
            linha += str(G[i][j]) + "|"
        linha+="\n"
    
    #Impressão da matriz de adjacências para o usuario
    print(linha)
DFS()
print("\nd: "+str(d))
print("f: "+str(f))
print("pi: "+str(pi))
print("c: "+str(color))