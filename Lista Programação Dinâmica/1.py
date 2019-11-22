def impressao(l,M):
  '''
  Parametros
  l -- Vetor contendo as palavras
  M -- numero de caracteres numa linha
  '''

  i=0
  linha=[""]
  for k in range (len(l)):
    if (len(linha[-1])+len(l[k])+1)>M:
      size = len(linha[-1]) #APAGAR ISSO DEPOIS
      linha[-1]+=str((M-len(linha[-1]))*" ")
      linha[-1]+="size = {}".format(size)
      linha.append(l[k]+" ")
    else:
      linha[-1]+=(l[k]+" ")
  return('\n'.join(linha))

s = (input("Sua frase aqui: ")).split(" ")
print(s)
print("\n\n{}".format(impressao(s,30)))
