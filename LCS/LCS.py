m = 0
n = 0
def LCS(X, Y): #Subsequência Comum Mais Longa (Longest Common Subsequence)
  global m,n
  m = len(X) #linhas
  n = len(Y) #colunas

  c = [[[0,""] for col in range(n+1)] for row in range(m+1)]
  """
  Aqui foi utilizada uma Compreensão de Lista, uma construção sintática disponível em algumas linguagens
  de programação (Exemplos: Python, Haskell) baseada em listas existentes. Neste caso, foi utilizada para
  gerar uma matriz de elementos [0,""], de (n+1) colunas e (m+1) linhas.
  """
  for i in range(1,m+1):
    for j in range(1,n+1):
      if X[i-1]==Y[j-1]:
        c[i][j][0]=int(c[i-1][j-1][0])+1
        c[i][j][1]=str(c[i-1][j-1][1])+X[i-1]
      else:
        c[i][j]=max([c[i-1][j],c[i][j-1]])

  b = [[c[row][col][0] for col in range(n+1)] for row in range(m+1)]
  return [b,c[m][n]]

x = input("Insira a sequencia x: ")
y = input("Insira a sequencia y: ")
retorno = LCS(x,y)
# retorno = LCS("ABCB","BDCAB")
print("Tamanho da LCS: {}; LCS: {}".format(retorno[1][0],retorno[1][1]))

print("\n".join(["".join(["{:{width}}".format(item, width = len(str(max(m,n)))+1) for item in row]) for row in retorno[0]]))
"""
Código adaptado do usuário unutbu do site stackoverflow
link para o perfil do mesmo: https://stackoverflow.com/users/190597/unutbu 
"""