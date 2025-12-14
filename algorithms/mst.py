import networkx as nx




def prim_mst(G):
return nx.minimum_spanning_tree(G, algorithm="prim")




def kruskal_mst(G):
return nx.minimum_spanning_tree(G, algorithm="kruskal")