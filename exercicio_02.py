from collections import deque


def contar_passeios_validos(
    S: int,
    tuneis: list[tuple[int, int]],
    passeios: list[list[int]]
) -> int:
    grafo = {i: [] for i in range(1, S + 1)}
    for x, y in tuneis:
        grafo[x].append(y)
        grafo[y].append(x)

    componente = {}
    visitados = set()
    comp_id = 0

    def bfs(inicio, cid):
        fila = deque([inicio])
        visitados.add(inicio)
        componente[inicio] = cid
        while fila:
            v = fila.popleft()
            for viz in grafo[v]:
                if viz not in visitados:
                    visitados.add(viz)
                    componente[viz] = cid
                    fila.append(viz)

    for v in range(1, S + 1):
        if v not in visitados:
            bfs(v, comp_id)
            comp_id += 1

    validos = 0
    for passeio in passeios:
        valido = all(
            componente[passeio[k]] == componente[passeio[k + 1]]
            for k in range(len(passeio) - 1)
        )
        if valido:
            validos += 1

    return validos


S, T = map(int, input().split())
tuneis = []
for _ in range(T):
    x, y = map(int, input().split())
    tuneis.append((x, y))

P = int(input())
passeios = []
for _ in range(P):
    linha = list(map(int, input().split()))
    passeios.append(linha[1:linha[0] + 1])

print(contar_passeios_validos(S, tuneis, passeios))
