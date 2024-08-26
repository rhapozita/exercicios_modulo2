#Exercicios:
#1. De acordo com o array X = np.array([3, 5, 6, 7, 2, 3, 4, 9, 4]) faça a soma
#2. Faça a média

X_1 = np.array([3, 5, 6, 7, 2, 3, 4, 9, 4])
soma = np.sum(X_1)
print(f'Soma do array: {soma}')

media = np.mean(X_1)
print(f'Média do array: {media}')

#3. Dada a matriz faça a soma das colunas X = np.array([
#    [1,   2,  3,  4],
#    [5,   6,  7,  8],
#    [9,  10, 11, 12],
#    [13, 14, 15, 16]
#])
#4. Faça a média das linhas

X_3 = np.array([
    [1,   2,  3,  4],
    [5,   6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])
soma_das_colunas = np.sum(X_3,axis=0)
print(f'A soma das colunas é: {soma_das_colunas}')

media_das_linhas = np.mean(X_3,axis=1)
print(f'A média das linhas é: {media_das_linhas}')

#5. Dado o array X = np.array([1, 2, 0, 4, 5, 6, 0, 0, 9, 10]) Mostre o elemento de maior valor

X_5 = np.array([1, 2, 0, 4, 5, 6, 0, 0, 9, 10])
X_5.max()
