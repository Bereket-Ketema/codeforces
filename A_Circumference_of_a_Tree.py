import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, graph, n):
    dist = [-1]*n
    q = deque([start])
    dist[start] = 0
    
    while q:
        u = q.popleft()
        for v in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    
    farthest = dist.index(max(dist))
    return farthest, max(dist)

def solve():
    n = int(input())
    
    if n == 1:
        print(0)
        return
    
    graph = [[] for _ in range(n)]
    
    for _ in range(n-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    
    node, _ = bfs(0, graph, n)
    
    _, diameter = bfs(node, graph, n)
    
    print(3 * diameter)

solve()