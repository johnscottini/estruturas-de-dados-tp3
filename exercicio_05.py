from collections import deque

arestas = [
    ("brush", "nail_polish"),
    ("nail_polish", "eye_shadow"),
    ("eye_shadow", "eye_glasses"),
    ("nail_polish", "nails"),
    ("nails", "pins"),
    ("nails", "needles"),
    ("pins", "needles"),
    ("nails", "hammer"),
    ("hammer", "drill"),
    ("hammer", "saw"),
    ("saw", "knife"),
    ("knife", "fork"),
    ("knife", "spoon"),
]

grafo = {}
for u, v in arestas:
    grafo.setdefault(u, []).append(v)
    grafo.setdefault(v, []).append(u)

for v in grafo:
    grafo[v].sort()


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


print("Ordem BFS:", " -> ".join(bfs("nails")))
