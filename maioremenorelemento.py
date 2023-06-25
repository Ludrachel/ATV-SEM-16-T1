def encontra_maior_menor(matriz):
    n = len(matriz)
    linha_maior = coluna_maior = linha_menor = coluna_menor = 0
    for i in range(n):
        for j in range(n):
            if matriz[i][j] > matriz[linha_maior][coluna_maior]:
                linha_maior, coluna_maior = i, j
            elif matriz[i][j] < matriz[linha_menor][coluna_menor]:
                linha_menor, coluna_menor = i, j
    return ((linha_maior, coluna_maior), (linha_menor, coluna_menor))

n = int(input())
matriz = [[int(input()) for j in range(n)] for i in range(n)]
maior_menor = encontra_maior_menor(matriz)
print(f"({maior_menor[0][0]}, {maior_menor[0][1]})")
print(f"({maior_menor[1][0]}, {maior_menor[1][1]})")
