import networkx as nx
import matplotlib.pyplot as plt
#G1=nx.complete_graph(10)
G1=nx.gnp_random_graph(20,0.5)
"""G=nx.Graph()
l=[1,2,3,4,5,6]
G.add_nodes_from(l)
G.add_edge(6,1)
G.add_edge(2,6)
G.add_edge(6,3)
G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(3,1)
G.add_edge(3,4)
G.add_edge(4,5)
print(G.nodes())
print(G.edges())
nx.draw(G)
plt.show()"""
nx.draw(G1)
plt.show()