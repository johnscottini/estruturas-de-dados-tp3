import sys
from collections import deque
sys.setrecursionlimit(10000)

arestas = [
    ("Inicio", "A"),
    ("Inicio", "B"),
    ("A", "C"),
    ("B", "C"),
    ("C", "D"),
    ("D", "E"),
    ("B", "F"),
    ("F", "E"),
]

grafo = {}
for u, v in arestas:
    grafo.setdefault(u, []).append(v)
    grafo.setdefault(v, [])

for v in grafo:
    grafo[v].sort()

visitados_dfs = set()
ordem_dfs = []


def dfs(v):
    visitados_dfs.add(v)
    ordem_dfs.append(v)
    for viz in grafo[v]:
        if viz not in visitados_dfs:
            dfs(viz)


def bfs(inicio):
    visitados = {inicio}
    fila = deque([inicio])
    ordem = []
    while fila:
        v = fila.popleft()
        ordem.append(v)
        for viz in grafo[v]:
            if viz not in visitados:
                visitados.add(viz)
                fila.append(viz)
    return ordem


dfs("Inicio")
print("DFS:", " -> ".join(ordem_dfs))
print("BFS:", " -> ".join(bfs("Inicio")))
