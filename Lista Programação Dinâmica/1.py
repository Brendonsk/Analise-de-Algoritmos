def impressao(l,M):
  '''
  Parametros
  l -- Vetor contendo as palavras
  M -- Numero de caracteres numa linha
  '''
  #Vetor contendo o tamanho, em caracteres, de cada palavra no vetor l
  tam_palavr = [len(l[i]) for i in range(len(l))]

  #Vetor contendo cada linha da saida da funcao
  linha = [""]

  #Vetor contendo o tamanho atual de cada linha do vetor 'linha'
  tam_linha = [0]
  
  for k in range (len(l)):
    if (tam_linha[-1]+tam_palavr[k])>M:
      '''
      Caso a insercao da proxima palavra exceda o limite de caracteres da linha atual, uma nova linha
      e adicionada a saida, e nela a palavra atual do vetor l (l[k]) e inserida
      '''
      linha[-1]+=str((M-tam_linha[-1])*" ")
      linha.append(l[k]+" ")
      tam_linha.append(tam_palavr[k]+1)
    else:
      '''
      Caso contrario, tal palavra e inserida na linha atual
      '''
      linha[-1]+=(l[k]+" ")
      tam_linha[-1]+=tam_palavr[k]+1
  return('\n'.join(linha))

m = int(input("Digite a quantidade maxima de caracteres em uma linha: "))
s = (input("Digite um paragrafo de texto: ")).split(" ")
print("\n{}".format(impressao(s,m)))
