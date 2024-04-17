"""
This module provides functions to calculate the maximum bipartite matching in a graph,
which is used to model and solve the real estate broker problem where clients are matched
with suitable houses based on their requirements.
"""

from collections import deque, defaultdict


def bfs(graph, match, dist, n):
    """
    Perform a breadth-first search to update distances to the unmatched vertex in the graph.

    Args:
    graph (defaultdict): The graph representing connections between nodes.
    match (dict): Current matching in the bipartite graph.
    dist (dict): Distance to the nearest unmatched node.
    n (int): Number of nodes in the first partition of the graph (clients).

    Returns:
    bool: True if there is an augmenting path, False otherwise.
    """
    queue = deque()
    for v in range(1, n + 1):
        if match[v] == 0:
            dist[v] = 0
            queue.append(v)
        else:
            dist[v] = float('inf')
    dist[0] = float('inf')
    while queue:
        v = queue.popleft()
        if dist[v] < dist[0]:
            for u in graph[v]:
                if dist[match[u]] == float('inf'):
                    dist[match[u]] = dist[v] + 1
                    queue.append(match[u])
    return dist[0] != float('inf')


def dfs(graph, match, dist, v):
    """
    Perform a depth-first search to find and augment paths in the graph.

    Args:
    graph (defaultdict): The graph representing connections between nodes.
    match (dict): Current matching in the bipartite graph.
    dist (dict): Distance to the nearest unmatched node.
    v (int): Current node being visited.

    Returns:
    bool: True if an augmenting path is found starting from node v, False otherwise.
    """
    if v != 0:
        for u in graph[v]:
            if dist[match[u]] == dist[v] + 1:
                if dfs(graph, match, dist, match[u]):
                    match[u] = v
                    match[v] = u
                    return True
        dist[v] = float('inf')
        return False
    return True


def max_bipartite_matching(graph, n):
    """
    Calculates the maximum number of bipartite matching from a graph.

    Args:
    graph (defaultdict): The graph representing connections between clients and houses.
    n (int): Number of clients.

    Returns:
    int: Maximum number of matchings.
    """
    match = defaultdict(int)
    dist = {}
    matching = 0
    while bfs(graph, match, dist, n):
        for v in range(1, n + 1):
            if match[v] == 0:
                if dfs(graph, match, dist, v):
                    matching += 1
    return matching


def real_estate_broker(clients, houses):
    """
    Solves the real estate broker problem by matching clients to houses based on requirements.

    Args:
    clients (list): List of tuples (required area, max price).
    houses (list): List of tuples (house area, price).

    Returns:
    int: The maximum number of clients that can be matched to suitable houses.
    """
    n = len(clients)  # number of clients
    m = len(houses)  # number of houses
    graph = defaultdict(list)
    for i, (req_area, max_price) in enumerate(clients, 1):
        for j, (area, price) in enumerate(houses, 1):
            if area > req_area and price <= max_price:
                graph[i].append(j + n)  # Offset house indices by n to separate client and house indices

    return max_bipartite_matching(graph, n)
