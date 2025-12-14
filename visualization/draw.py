import matplotlib.pyplot as plt
from PIL import Image
import networkx as nx




def draw_graph(G, pos, bg_image,
highlight_nodes=None,
highlight_edges=None):


fig, ax = plt.subplots(figsize=(8, 8))


img = Image.open(bg_image)
ax.imshow(img)
ax.axis('off')


nx.draw(
G, pos,
with_labels=True,
node_color='lightblue',
node_size=1500,
font_size=9,
ax=ax
)


if highlight_nodes:
nx.draw_networkx_nodes(
G, pos,
nodelist=highlight_nodes,
node_color='orange',
node_size=1600,
ax=ax
)


if highlight_edges:
nx.draw_networkx_edges(
G, pos,
edgelist=highlight_edges,
edge_color='red',
width=4,
ax=ax
)


return fig