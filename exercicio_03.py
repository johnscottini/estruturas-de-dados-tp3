from collections import deque


def conectados(grafo, a, b):
    if a == b:
        return True
    visitados = {a}
    fila = deque([a])
    while fila:
        v = fila.popleft()
        for viz in grafo[v]:
            if viz == b:
                return True
            if viz not in visitados:
                visitados.add(viz)
                fila.append(viz)
    return False


N, M = map(int, input().split())
grafo = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    linha = list(map(int, input().split()))
    tipo, a, b = linha[0], linha[1], linha[2]
    if tipo == 1:
        grafo[a].append(b)
        grafo[b].append(a)
    else:
        print(1 if conectados(grafo, a, b) else 0)
