def LCS(X, Y): #Longest Common Subsequence
  m = len(X) #linhas
  n = len(Y) #colunas
  c = [[[0,""] for col in range(n+1)] for row in range(m+1)]
  for i in range(1,m+1):
    for j in range(1,n+1):
      if X[i-1]==Y[j-1]:
        c[i][j][0]=int(c[i-1][j-1][0])+1
        c[i][j][1]=str(c[i-1][j-1][0])+X[i-1]
      else:
        c[i][j]=max([c[i-1][j],c[i][j-1]])
  return c[m][n]

retorno = LCS("ABCB","BDCAB")
print("{}\n{}".format(retorno[0],retorno[1]))