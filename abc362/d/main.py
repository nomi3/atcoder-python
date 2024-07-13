import heapq

N, M = map(int, input().split())
A = list(map(int, input().split()))

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, b = map(int, input().split())
    graph[u].append((v, b))
    graph[v].append((u, b))

def dijkstra(start):
    dist = [float('inf')] * (N + 1)
    dist[start] = A[start - 1]
    pq = [(A[start - 1], start)]

    while pq:
        current_dist, u = heapq.heappop(pq)
        if current_dist > dist[u]:
            continue
        for v, weight in graph[u]:
            next_dist = current_dist + weight + A[v - 1]
            if next_dist < dist[v]:
                dist[v] = next_dist
                heapq.heappush(pq, (next_dist, v))

    return dist

dist_from_1 = dijkstra(1)

result = [dist_from_1[i] for i in range(2, N + 1)]
print(" ".join(map(str, result)))