import sys
sys.setrecursionlimit(10000)

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

visitados = set()
ordem = []


def dfs(v):
    visitados.add(v)
    ordem.append(v)
    for viz in grafo[v]:
        if viz not in visitados:
            dfs(viz)


dfs("nails")
print("Ordem DFS:", " -> ".join(ordem))
