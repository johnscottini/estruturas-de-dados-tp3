import heapq

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


def dijkstra(origem):
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

    return dist, pred


dist, pred = dijkstra("Berco_A")

print("Menores distancias a partir de Berco_A:")
for v in sorted(dist):
    if v != "Berco_A":
        print(f"  {v}: {dist[v]}")
