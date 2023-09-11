# Algoritmi di routing sui grafi:
    # Algoritmo di dijkstra

import heapq

def dijkstra(graph, start):
    # Inizializzazione delle distanze da 'start' a tutti gli altri nodi a infinito.
    # Inizializzazione del dizionario 'distances' con le distanze.
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Coda con priorità per mantenere traccia dei nodi da esplorare.
    priority_queue = [(0, start)]

    while priority_queue:
        # Estrai il nodo con la distanza minima dalla coda.
        current_distance, current_node = heapq.heappop(priority_queue)

        # Se abbiamo già esaminato questo nodo con una distanza minore,
        # ignoralo e continua con il prossimo.
        if current_distance > distances[current_node]:
            continue

        # Esamina i vicini del nodo corrente.
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Se abbiamo trovato un percorso più breve verso il vicino, aggiorna la distanza.
            if distance < distances[neighbor]:
                distances[neighbor] = distance

                # Aggiungi il vicino alla coda con priorità.
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Esempio di utilizzo:
if __name__ == "__main__":
    # Definizione del grafo con pesi degli archi.
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    start_node = 'A'
    shortest_distances = dijkstra(graph, start_node)

    print("Distanze minime dai nodi di partenza:")
    for node, distance in shortest_distances.items():
        print(f"{node}: {distance}")