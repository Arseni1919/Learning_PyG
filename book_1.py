import networkx as nx
import pandas as pd
import numpy as np

g= nx.Graph()

v = {'d', 'p', 'm', 'r'}
e = [
    ('m', 'd'),
    ('m', 'p'),
    ('p', 'd'),
    ('m', 'r')
]

g.add_nodes_from(v)
g.add_edges_from(e)

print(g.nodes)
