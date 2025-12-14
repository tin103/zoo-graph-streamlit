import networkx as nx


# Tọa độ các khu (theo ảnh Thảo Cầm Viên)
zoo_nodes = {
"Cổng chính": (0.1, 0.9),
"Khu Hổ": (0.4, 0.8),
"Khu Voi": (0.7, 0.7),
"Nhà Bò Sát": (0.8, 0.4),
"Khu Khỉ": (0.3, 0.5),
"Khu Chim": (0.6, 0.5)
}


edges = [
("Cổng chính", "Khu Hổ", 120),
("Cổng chính", "Khu Khỉ", 150),
("Khu Hổ", "Khu Voi", 180),
("Khu Voi", "Nhà Bò Sát", 100),
("Khu Khỉ", "Khu Chim", 130),
("Khu Chim", "Khu Hổ", 160)
]




def create_graph():
G = nx.Graph()
for node in zoo_nodes:
G.add_node(node)
for u, v, w in edges:
G.add_edge(u, v, weight=w)
return G, zoo_nodes