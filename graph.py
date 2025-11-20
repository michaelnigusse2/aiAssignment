import math

def load_graph(filename):

    graph = {}
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split()
            if len(parts) != 3:
                continue
            a, b, cost = parts
            try:
                c = float(cost)
            except ValueError:
                continue
            graph.setdefault(a, {})[b] = c
            graph.setdefault(b, {})[a] = c
    return graph

def load_heuristic(filename):

    h = {}
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split()
            if len(parts) != 3:
                continue
            a, b, val = parts
            try:
                v = float(val)
            except ValueError:
                continue
            h[(a, b)] = v
            h[(b, a)] = v
    return h

def heuristic_lookup(heur_dict, node, goal):

    return heur_dict.get((node, goal), 0.0)
