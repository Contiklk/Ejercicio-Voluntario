from collections import deque
import time

mapa_arrakis = {
    "Arrakeen": ["Sietch Tabr", "Oasis del Norte", "Campamento Fremen"],
    "Sietch Tabr": ["Arrakeen", "Oasis del Este", "Montaña de la Especia"],
    "Oasis del Norte": ["Arrakeen", "Campamento Fremen"],
    "Campamento Fremen": ["Arrakeen", "Oasis del Norte", "Oasis del Este"],
    "Oasis del Este": ["Sietch Tabr", "Campamento Fremen", "Zona Peligrosa"],
    "Montaña de la Especia": ["Sietch Tabr", "Zona Peligrosa"],
    "Zona Peligrosa": ["Oasis del Este", "Montaña de la Especia"]
}

def bfs_ruta_mas_corta(grafo, origen, destino):
    cola = deque([[origen]])
    visitados = set()

    while cola:
        ruta = cola.popleft()
        nodo = ruta[-1]

        if nodo == destino:
            print(f"Ruta más corta de {origen} a {destino}: {ruta}")
            print(f"Distancia total: {len(ruta)}")
            return ruta

        if nodo not in visitados:
            visitados.add(nodo)
            for vecino in grafo[nodo]:
                nueva_ruta = list(ruta)
                nueva_ruta.append(vecino)
                cola.append(nueva_ruta)

def dfs_conectividad(grafo, nodo, visitados):
    visitados.add(nodo)
    for vecino in grafo[nodo]:
        if vecino not in visitados:
            dfs_conectividad(grafo, vecino, visitados)

def es_conexo(grafo):
    visitados = set()
    inicio = next(iter(grafo))
    dfs_conectividad(grafo, inicio, visitados)
    if len(visitados) == len(grafo):
        print("El grafo es conexo.")
    else:
        print("El grafo NO es conexo.")

def bfs_rutas_seguras(grafo, origen, destino, evitar):
    rutas_seguras = []
    cola = deque([[origen]])
    while cola:
        ruta = cola.popleft()
        nodo = ruta[-1]

        if nodo == destino:
            rutas_seguras.append(ruta)
            continue

        for vecino in grafo[nodo]:
            if vecino not in ruta and vecino != evitar:
                nueva_ruta = list(ruta)
                nueva_ruta.append(vecino)
                cola.append(nueva_ruta)

    print(f"Rutas seguras desde {origen} a {destino} sin pasar por '{evitar}':")
    for r in rutas_seguras:
        print(r)
    return rutas_seguras

def dfs_melange(grafo, nodo, visitados):
    visitados.add(nodo)
    print(nodo)
    for vecino in grafo[nodo]:
        if vecino not in visitados:
            dfs_melange(grafo, vecino, visitados)

def buscar_melange(grafo, origen):
    print("Orden de exploración de Melange:")
    visitados = set()
    dfs_melange(grafo, origen, visitados)

def analizar_eficiencia():
    inicio_bfs = time.time()
    bfs_ruta_mas_corta(mapa_arrakis, "Arrakeen", "Oasis del Norte")
    print("Tiempo BFS:", time.time() - inicio_bfs)

    inicio_dfs = time.time()
    buscar_melange(mapa_arrakis, "Arrakeen")
    print("Tiempo DFS:", time.time() - inicio_dfs)

    print("\nAnálisis:")
    print("BFS es ideal para encontrar rutas más cortas.")
    print("DFS es útil para explorar todas las rutas posibles.")

print("\n--- Tarea 1 ---")
bfs_ruta_mas_corta(mapa_arrakis, "Arrakeen", "Oasis del Norte")

print("\n--- Tarea 2 ---")
es_conexo(mapa_arrakis)

print("\n--- Tarea 3 ---")
bfs_rutas_seguras(mapa_arrakis, "Arrakeen", "Montaña de la Especia", "Zona Peligrosa")

print("\n--- Tarea 4 ---")
buscar_melange(mapa_arrakis, "Arrakeen")

print("\n--- Tarea 5 ---")
analizar_eficiencia()