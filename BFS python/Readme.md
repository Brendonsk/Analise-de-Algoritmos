# Análise de custo BFS

- Análise do pior caso

Dado um grafo G(v,e) qualquer:

O loop das linhas 27-31 atribui valores aos vetores "color", "d" e "pi" para as posições cujos índices representam os vértices do grafo que não são iguais ao vértice de origem s, possuindo custo total de 4v-2 e,  portanto, possui complexidade O(v)

O while das linhas 46 a 60 refere-se ao enfileiramento dos vértices do grafo cujo índice, no vetor color, são representados por 'w'(white), seguindo uma exploração em largura. Portanto, o pior caso ocorre quando o vértice origem está conectado a apenas um outro vértice, que por sua vez está conectado ao vértice de origem e a outro vértice, diferente dos vértices anteriores, seguindo um padrão de vértices conectados a dois outros vértices, até que o último vértice, que será conectado a apenas o vértice o qual já foi explorado, for explorado. Neste caso, a complexidade do while é igual a O(v).

O for das lnhas 53 a 59 possui complexidade fixa de O(v²), pois ele sempre fará v iterações, sendo (v-1) para o meio do loop, e v para o início dele, e ele está dentro do loop while, de complexidade O(v).

Com isso, é possível concluir que a complexidade do algoritmo BFS em seu pior caso é 

Referência Bibliográfica: CORMEN, Thomas H.; LEISERSON, Charles E.; RIVEST, Ronald L.
Introduction to algorithms. New York: Mcgraw-hill book, 1990. 1028 p. ISBN
0262530910.
