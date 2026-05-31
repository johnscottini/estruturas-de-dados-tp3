import heapq
from collections import deque

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


def bfs_caminho(origem, destino):
    visitados = {origem}
    fila = deque([(origem, [origem])])
    while fila:
        v, caminho = fila.popleft()
        if v == destino:
            return caminho
        for viz, _ in grafo[v]:
            if viz not in visitados:
                visitados.add(viz)
                fila.append((viz, caminho + [viz]))
    return None


def dijkstra_caminho(origem, destino):
    dist = {v: float("inf") for v in grafo}
    dist[origem] = 0
    pred = {v: None for v in grafo}
    pq = [(0, origem)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in grafo[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                pred[v] = u
                heapq.heappush(pq, (dist[v], v))
    caminho = []
    v = destino
    while v is not None:
        caminho.append(v)
        v = pred[v]
    return list(reversed(caminho)), dist[destino]


def custo(caminho):
    total = 0
    for i in range(len(caminho) - 1):
        u, v = caminho[i], caminho[i + 1]
        total += next(w for viz, w in grafo[u] if viz == v)
    return total


caminho_bfs = bfs_caminho("Berco_A", "Centro_Logistico")
caminho_dijk, custo_dijk = dijkstra_caminho("Berco_A", "Centro_Logistico")

print("Caminho BFS:", " -> ".join(caminho_bfs))
print("Custo BFS:", custo(caminho_bfs))
print()
print("Caminho Dijkstra:", " -> ".join(caminho_dijk))
print("Custo Dijkstra:", custo_dijk)
