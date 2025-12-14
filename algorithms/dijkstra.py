import networkx as nx




def shortest_path(G, start, end):
return nx.dijkstra_path(G, start, end, weight="weight")