

import heapq
from queue import PriorityQueue
import networkx as nx
import matplotlib.pyplot as plt

# Función para encontrar el árbol de expansión mínima de un grafo
def prim(graph, start):
    visited = set([start])
    edges = [(cost, start, neighbor) for neighbor, cost in graph[start].items()]
    heapq.heapify(edges)
    G = nx.Graph()
    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            G.add_edge(frm, to, weight=cost)
            for neighbor, cost in graph[to].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (cost, to, neighbor))
    return G

# Crea un grafo de 10 nodos
graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1},
    'C': {'A': 3, 'B': 1},
    'D': {'E': 4},
    'E': {'D': 4, 'F': 5},
    'F': {'E': 5, 'G': 6},
    'G': {'F': 6, 'H': 7},
    'H': {'G': 7, 'I': 8},
    'I': {'H': 8, 'J': 9},
    'J': {'I': 9}
}


G = prim(graph, 'J')
print(G)

# Encuentra el árbol de expansión mínima del grafo


# Dibuja el grafo y las etiquetas de las aristas
pos = nx.spring_layout(G)
nx.draw(G, pos)
nx.draw_networkx_edge_labels(G,pos=nx.spring_layout(G),edge_labels=nx.get_edge_attributes(G,'weight'))
plt.show()