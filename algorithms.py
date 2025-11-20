
import heapq

def ucs_steps(start, goal, graph):

    frontier = [(0.0, start, [start])]
    closed = set()
    while frontier:
        cost, node, path = heapq.heappop(frontier)
        if node in closed:
            continue
        closed.add(node)
        frontier_nodes = [n for _, n, _ in frontier]
        yield node, frontier_nodes, set(closed), path, cost
        if node == goal:
            return
        for neighbor, edge_cost in graph.get(node, {}).items():
            if neighbor not in closed:
                heapq.heappush(frontier, (cost + edge_cost, neighbor, path + [neighbor]))

def astar_steps(start, goal, graph, heuristic_func):

    g0 = 0.0
    f0 = g0 + heuristic_func(start, goal)
    frontier = [(f0, g0, start, [start])]
    closed = set()
    while frontier:
        f, g, node, path = heapq.heappop(frontier)
        if node in closed:
            continue
        closed.add(node)
        frontier_nodes = [tpl[2] for tpl in frontier]
        yield node, frontier_nodes, set(closed), path, g
        if node == goal:
            return
        for neighbor, cost in graph.get(node, {}).items():
            if neighbor in closed:
                continue
            g_new = g + cost
            f_new = g_new + heuristic_func(neighbor, goal)
            heapq.heappush(frontier, (f_new, g_new, neighbor, path + [neighbor]))
