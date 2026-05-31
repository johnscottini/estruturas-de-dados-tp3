import heapq
import sys
from collections import deque
sys.setrecursionlimit(10000)

arestas = [
    ("Berco_A", "Patio_1", 4),
    ("Berco_A", "Patio_2", 7),
    ("Berco_B", "Patio_2", 3),
    ("Berco_B", "Patio_3", 6),
    ("Patio_1", "Patio_2", 2),
    ("Patio_2", "Patio_3", 2),
    ("Patio_1", "Alfandega", 8),
    ("Patio_2", "Alfandega", 5),
    ("Patio_3", "Centro_Logistico", 4),
    ("Alfandega", "Centro_Logistico", 3),
]

grafo = {}
for u, v, w in arestas:
    grafo.setdefault(u, []).append((v, w))
    grafo.setdefault(v, []).append((u, w))

for v in grafo:
    grafo[v].sort(key=lambda x: x[0])


def dfs(inicio):
    visitados = set()
    ordem = []

    def _dfs(v):
        visitados.add(v)
        ordem.append(v)
        for viz, _ in grafo[v]:
            if viz not in visitados:
                _dfs(viz)

    _dfs(inicio)
    return ordem


def bfs(inicio):
    visitados = {inicio}
    fila = deque([inicio])
    ordem = []
    while fila:
        v = fila.popleft()
        ordem.append(v)
        for viz, _ in grafo[v]:
            if viz not in visitados:
                visitados.add(viz)
                fila.append(viz)
    return ordem


def dijkstra(origem):
    dist = {v: float("inf") for v in grafo}
    dist[origem] = 0
    pq = [(0, origem)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in grafo[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist


ordem_dfs = dfs("Berco_A")
ordem_bfs = bfs("Berco_A")
distancias = dijkstra("Berco_A")

print("DFS:", " -> ".join(ordem_dfs))
print("BFS:", " -> ".join(ordem_bfs))
print("\nDistancias minimas (Dijkstra) a partir de Berco_A:")
for v in sorted(distancias):
    if v != "Berco_A":
        print(f"  {v}: {distancias[v]}")
