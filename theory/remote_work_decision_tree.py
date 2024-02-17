# Full corrected code to generate a more complex and visually appealing flowchart resembling a binary tree

import matplotlib.pyplot as plt
import networkx as nx

# Initialize the directed graph
G = nx.DiGraph()

# Nodes with additional decisions, excluding "End Day" and highlighting final decisions in green
# Define a corrected set of nodes with "Go to Work" highlighted and without an unconnected "Work Remotely"
nodes = {
    "Start": {"pos": (2, 8), "label": "Start\nDay"},
    "TFL Working?": {"pos": (2, 7), "label": "TFL\nWorking\nFine?"},
    "Weather Good?": {"pos": (1, 6), "label": "Weather\nGood?"},
    "Go to Work": {"pos": (0, 5), "label": "Go to\nWork", "color": "lightgreen"},  # Highlighted
    "Stay Home": {"pos": (4, 5), "label": "Work\nRemotely", "color": "skyblue"},  # Corrected to ensure it's connected
    "Important Meeting?": {"pos": (0.5, 4), "label": "Important\nMeeting?"},
    "Meeting Online?": {"pos": (3.5, 4), "label": "Meeting\nOnline?"},
    "Attend Meeting": {"pos": (0, 3), "label": "Attend\nMeeting", "color": "lightgreen"},
    "Skip Meeting": {"pos": (1, 3), "label": "Skip\nMeeting", "color": "lightgreen"},
    "Work Remotely": {"pos": (3, 3), "label": "Work\nRemotely", "color": "lightgreen"},  #
    "Take Day Off": {"pos": (4, 3), "label": "Take\nDay Off", "color": "lightgreen"},
}

# Re-adding nodes with corrected attributes
for node, info in nodes.items():
    G.add_node(node, pos=info["pos"], label=info["label"], color=info.get("color", "skyblue"))


# Define edges with decisions
edges = [
    ("Start", "TFL Working?"),
    ("TFL Working?", "Weather Good?", "Yes"),
    ("Weather Good?", "Go to Work", "Yes"),
    ("Weather Good?", "Important Meeting?", "No"),
    ("TFL Working?", "Meeting Online?", "No"),
    ("Important Meeting?", "Attend Meeting", "Yes"),
    ("Important Meeting?", "Skip Meeting", "No"),
    ("Meeting Online?", "Work Remotely", "Yes"),
    ("Meeting Online?", "Take Day Off", "No"),
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
nx.draw_networkx_edges(G, pos, edge_color="blue", arrowstyle="-|>", arrowsize=20)

# Drawing edge labels with green for "Yes" and red for "No"
edge_labels = nx.get_edge_attributes(G, 'label')
for edge, label in edge_labels.items():
    label_color = "green" if label == "Yes" else "red"
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(edge[0], edge[1]): label}, font_color=label_color)

plt.axis('off')
plt.tight_layout()
plt.show()