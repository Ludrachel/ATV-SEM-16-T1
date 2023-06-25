n = int(input())
m = int(input())

matriz = []
for i in range(n):
    linha = []
    for j in range(m):
        valor = int(input())
        linha.append(valor)
    matriz.append(linha)

soma_primeira_linha = sum(matriz[0])
soma_ultima_coluna = sum([linha[-1] for linha in matriz])
media_elementos = sum([sum(linha) for linha in matriz]) / (n*m)
menor_elemento = min([min(linha) for linha in matriz])
maior_elemento = max([max(linha) for linha in matriz])

print(f'({soma_primeira_linha}, {soma_ultima_coluna}, {round(media_elementos, 4)}, {menor_elemento}, {maior_elemento})')

