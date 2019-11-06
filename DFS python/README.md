# Análise de custo DFS

Analisando o custo desse procedimento para um grafo G(V,E):

O procedimento DFS() possui o custo do loop das linhas 22-26 é executado V vezes, pois depende da quantidade de vértices do grafo para atribuir aos vetores do loop os valores iniciais\; somado ao custo do procedimento DFS_visita, que, por sua vez, possui o custo de E, considerando que ele é chamado uma vez para os vertices adjacentes de cada vértice v pertencente ao grafo G, e que os vértices já explorados em iterações anteriores nao são explorados novamente.
Com isso, somando V+E, conclui-se que a complexidade para o procedimento DFS é Θ(V+E), pois o pior caso é igual ao melhor caso, que também significa que o custo a execução deste procedimento com dois Grafos distintgs, mas que possuem o mesmo número de arestas e vértices, é idêntico.

Referência Bibliográfica: CORMEN, Thomas H.; LEISERSON, Charles E.; RIVEST, Ronald L.
Introduction to algorithms. New York: Mcgraw-hill book, 1990. 1028 p. ISBN
0262530910.