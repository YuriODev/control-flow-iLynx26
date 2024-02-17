# Full corrected code to generate a more complex and visually appealing flowchart resembling a binary tree

import matplotlib.pyplot as plt
import networkx as nx

# Initialize the directed graph
G = nx.DiGraph()

# Define a complex decision-making scenario for Liverpool FC players on the football field


# Nodes for the football decision-making scenario
nodes = {
    "Salah": {"pos": (5, 10), "label": "Salah\nwith\nthe\nBall"},
    "Salah Marked?": {"pos": (5, 9), "label": "Is\nSalah\n marked?"},
    "Pass to Mané": {"pos": (3, 8), "label": "Pass\nto\nMané"},
    "Mané Shoot": {"pos": (2, 7), "label": "Mané\nShoots", "color": "lightgreen"},
    "Mané to TAA": {"pos": (4, 7), "label": "Pass\nto\nTAA", "color": "lightgreen"},
    "Salah Dribble": {"pos": (7, 8), "label": "Salah\nDribbles"},
    "Salah Cross": {"pos": (6, 7), "label": "Salah\nCrosses"},
    "Firmino Header": {"pos": (5, 6), "label": "Firmino\nHeader", "color": "lightgreen"},
    "Firmino Volley": {"pos": (7, 6), "label": "Firmino\nVolley", "color": "lightgreen"},
    "Pass to Hendo": {"pos": (8, 6), "label": "Pass\nto\nHenderson"},
    "Hendo Shot": {"pos": (8, 5), "label": "Henderson\nLong\nShot", "color": "lightgreen"},
    "Reset Attack": {"pos": (9, 5), "label": "Reset\nAttack", "color": "lightgreen"},
    "Salah Run": {"pos": (10, 7), "label": "Salah\nSolo\nRun", "color": "lightgreen"},
    "Pass to Thiago": {"pos": (11, 8), "label": "Pass\nto\nThiago", "color": "lightgreen"},

}

for node, info in nodes.items():
    G.add_node(node, pos=info["pos"], label=info["label"], color=info.get("color", "skyblue"))


# Define edges for the football scenario
edges = [
    ("Salah", "Salah Marked?", ""),
    ("Salah Marked?", "Pass to Mané", "Yes"),
    ("Pass to Mané", "Mané Shoot", "Good Position"),
    ("Pass to Mané", "Mané to TAA", "No Shot"),
    ("Salah Marked?", "Salah Dribble", "No"),
    ("Salah Dribble", "Salah Cross", "Space"),
    ("Salah Cross", "Firmino Header", "Header"),
    ("Salah Cross", "Firmino Volley", "Volley"),
    ("Salah Dribble", "Pass to Hendo", "No Cross"),
    ("Pass to Hendo", "Hendo Shot", "Clear Path"),
    ("Pass to Hendo", "Reset Attack", "No Path"),
    ("Salah Marked?", "Salah Run", "Space"),
    ("Salah Marked?", "Pass to Thiago", "No Space")
    
]


# Add edges to the graph
for edge in edges:
    G.add_edge(*edge[:2], label=edge[2] if len(edge) > 2 else "")


# Set positions
pos = nx.get_node_attributes(G, 'pos')
labels = nx.get_node_attributes(G, 'label')
edge_labels = nx.get_edge_attributes(G, 'label')

# Drawing the flowchart
plt.figure(figsize=(12, 9))

# Drawing nodes with specific colors
node_colors = [G.nodes[node]["color"] for node in G.nodes()]
nx.draw_networkx_nodes(G, pos, node_size=3500, node_color=node_colors, edgecolors="black", linewidths=2)

# Labels with normal font weight
nx.draw_networkx_labels(G, pos, labels=labels, font_size=10)

# Drawing edges
nx.draw_networkx_edges(G, pos, edge_color="blue", arrowstyle="-|>", arrowsize=20, width=0.5)

# Drawing edge labels with green for "Yes" and red for "No"
edge_labels = nx.get_edge_attributes(G, 'label')
for edge, label in edge_labels.items():
    label_color = "red" if "No" in label else "green"
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(edge[0], edge[1]): label}, font_color=label_color)

plt.axis('off')
plt.tight_layout()
plt.show()