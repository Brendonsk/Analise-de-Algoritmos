# Análise de custo LCS

As atribuições a m e n possuem custo de 1 cada.
O primeiro loop possui complexidade m, pois ele itera a string X.
O segundo loop possui complexidade n, pois ele itera a string Y.

O terceiro loop, que contém também o quarto dentro dele, possui custo de 2*\m\*n, pois ele itera a string X no terceiro loop, que dentro dele também itera a string Y, e, independente de a condição do if ser falsa ou verdadeira, serão feitas duas operações dentro do quarto loop

Somando os custos,tem-se m + n + 2*\m*\n, portanto, a complexidade dele é Θ(m\*n)