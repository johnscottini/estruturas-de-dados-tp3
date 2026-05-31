import sys
sys.setrecursionlimit(10000)


def contar_grupos(n, arestas):
    grafo = {i: [] for i in range(1, n + 1)}
    for i, j in arestas:
        grafo[i].append(j)
        grafo[j].append(i)

    visitados = set()
    grupos = 0

    def dfs(v):
        visitados.add(v)
        for viz in grafo[v]:
            if viz not in visitados:
                dfs(viz)

    for v in range(1, n + 1):
        if v not in visitados:
            dfs(v)
            grupos += 1

    return grupos


n, m = map(int, input().split())
arestas = []
for _ in range(m):
    i, j = map(int, input().split())
    arestas.append((i, j))

print(contar_grupos(n, arestas))
