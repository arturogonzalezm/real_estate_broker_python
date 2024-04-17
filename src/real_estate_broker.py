from collections import deque, defaultdict


def bfs(graph, match, dist, N):
    queue = deque()
    for v in range(1, N + 1):
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


def max_bipartite_matching(graph, N, M):
    match = defaultdict(int)
    dist = {}
    matching = 0
    while bfs(graph, match, dist, N):
        for v in range(1, N + 1):
            if match[v] == 0:
                if dfs(graph, match, dist, v):
                    matching += 1
    return matching


def real_estate_broker(clients, houses):
    n = len(clients)  # number of clients
    m = len(houses)  # number of houses
    graph = defaultdict(list)
    for i, (req_area, max_price) in enumerate(clients, 1):
        for j, (area, price) in enumerate(houses, 1):
            if area > req_area and price <= max_price:
                graph[i].append(j + n)  # Offset house indices by n to separate client and house indices

    return max_bipartite_matching(graph, n, m)
