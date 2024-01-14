from heapq import heappush, heappop
import math


def dijkstra(
    graph,
    initial,
    final=None,
    distances=None,
    heuristic=lambda node1, node2: 0,
):
    # find shortest path starting from initial node to final node
    # if there is no final node, returns shortest path to every reachable node
    # complexity: O(E.log(N))

    colors = {}
    _distances = {}
    prec = {}
    for n in graph.keys():
        colors[n] = 0
        _distances[n] = float("inf")

    heap = [(0, initial)]
    _distances[initial] = 0
    prec[initial] = None

    while heap:
        _, node = heappop(heap)
        if node == final:
            path = [node]
            while prec[node]:
                node = prec[node]
                path.append(node)
            path.reverse()
            return _distances[final], path
        if colors[node] == 0:
            colors[node] = 1
            for neighbour in graph[node]:
                d = _distances[node] + distances.get((node, neighbour), 1)
                if d < _distances[neighbour]:
                    prec[neighbour] = node
                    heappush(heap, (d + heuristic(neighbour, final), neighbour))
                    _distances[neighbour] = d
    if final == None:
        return _distances, prec
    return float("inf"), []


def manhattan_heuristic(node1, node2):
    i1, j1 = node1
    i2, j2 = node2
    return abs(i2 - i1) + abs(j2 - j1)


def a_star_manhattan(graph, initial, final, distances):
    return dijkstra(graph, initial, final, distances, manhattan_heuristic)


def euclidean_heuristic(node1, node2):
    i1, j1 = node1
    i2, j2 = node2
    return math.sqrt((i2 - i1) ** 2 + (j2 - j1) ** 2)


def a_star_euclidean(graph, initial, final, distances):
    return dijkstra(graph, initial, final, distances, euclidean_heuristic)
