# Algoritmi di classificazione sui grafi
    # Algoritmo di propagazione delle etichette (Label Propagation)

import networkx as nx

# Creazione di un grafo non diretto con NetworkX
G = nx.Graph()

# Aggiungi nodi al grafo
G.add_nodes_from([1, 2, 3, 4, 5])

# Aggiungi archi al grafo (connettendo i nodi)
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5)])

# Inizializza le etichette dei nodi (in questo caso, numeri casuali)
import random
for node in G.nodes:
    G.nodes[node]['label'] = random.randint(0, 1)

# Funzione per eseguire un passaggio di propagazione delle etichette
def label_propagation_step(graph):
    new_labels = {}
    
    for node in graph.nodes:
        neighbors = list(graph.neighbors(node))
        neighbor_labels = [graph.nodes[neighbor]['label'] for neighbor in neighbors]
        
        # Calcola la nuova etichetta come etichetta più frequente tra i vicini
        if neighbor_labels:
            new_label = max(neighbor_labels, key=neighbor_labels.count)
            new_labels[node] = new_label
        else:
            # Se il nodo non ha vicini, mantieni l'etichetta attuale
            new_labels[node] = graph.nodes[node]['label']
    
    # Aggiorna le etichette dei nodi con le nuove etichette calcolate
    for node, label in new_labels.items():
        graph.nodes[node]['label'] = label

# Esegui l'algoritmo di propagazione delle etichette per un numero di iterazioni
num_iterations = 5
for i in range(num_iterations):
    label_propagation_step(G)

# Stampa le etichette finali dei nodi
for node in G.nodes:
    print(f'Nodo {node}: Etichetta {G.nodes[node]["label"]}')


# Questo codice illustra l'algoritmo di propagazione delle etichette su un grafo semplice. 
# Inizia creando un grafo non diretto, assegna etichette casuali ai nodi 
# e quindi esegue iterativamente il passaggio di propagazione delle etichette 
# fino a quando le etichette convergono o fino a quando viene raggiunto un numero massimo di iterazioni. 
# Alla fine, verranno stampate le etichette finali dei nodi.