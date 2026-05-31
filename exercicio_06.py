from collections import deque

conexoes = [
    ("Idris", "Kamil"),
    ("Idris", "Talia"),
    ("Kamil", "Lina"),
    ("Lina", "Sasha"),
    ("Sasha", "Marco"),
    ("Marco", "Ken"),
    ("Ken", "Talia"),
]

grafo = {}
for u, v in conexoes:
    grafo.setdefault(u, []).append(v)
    grafo.setdefault(v, []).append(u)


def menor_caminho(inicio, fim):
    visitados = {inicio}
    fila = deque([(inicio, [inicio])])
    while fila:
        v, caminho = fila.popleft()
        if v == fim:
            return caminho
        for viz in grafo[v]:
            if viz not in visitados:
                visitados.add(viz)
                fila.append((viz, caminho + [viz]))
    return None


caminho = menor_caminho("Idris", "Lina")
print("Caminho:", " -> ".join(caminho))
print("Distancia:", len(caminho) - 1, "conexoes")
