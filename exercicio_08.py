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


def bfs(origem):
    visitados = {origem}
    fila = deque([origem])
    predecessores = {origem: None}
    while fila:
        v = fila.popleft()
        for viz, _ in grafo[v]:
            if viz not in visitados:
                visitados.add(viz)
                predecessores[viz] = v
                fila.append(viz)
    return visitados, predecessores


def reconstruir(predecessores, destino):
    caminho = []
    v = destino
    while v is not None:
        caminho.append(v)
        v = predecessores[v]
    return list(reversed(caminho))


def custo_caminho(caminho):
    total = 0
    for i in range(len(caminho) - 1):
        u, v = caminho[i], caminho[i + 1]
        total += next(w for viz, w in grafo[u] if viz == v)
    return total


alcancaveis, predecessores = bfs("Berco_A")

print("Areas alcancaveis a partir de Berco_A:")
print(", ".join(sorted(alcancaveis)))

caminho = reconstruir(predecessores, "Centro_Logistico")
print("\nMenor caminho por etapas (BFS):", " -> ".join(caminho))
print("Numero de etapas:", len(caminho) - 1)
print("Custo total:", custo_caminho(caminho))
print("\nEsse caminho nao e necessariamente o de menor custo operacional.")
print("BFS ignora os pesos das arestas e trata todas as conexoes como equivalentes.")
print("Um caminho com mais etapas pode ter custo total menor se os pesos forem menores.")
