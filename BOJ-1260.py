# BOJ-1260.py

# DFS (Depth First Search)
# DFS 는 stack 자료구조 혹은 재귀함수를 이용한다.
def dfs(graph, v, visited):
    visited[v] = True # 방문처리
    print(v, end=" ")
    for node in graph[v]: # 인접 노드 반복
        if not visited[node]:
            dfs(graph, node, visited) # DFS 수행


# BFS (Breath First Search)
# BFS 는 queue 자료구조를 이용한다.
from collections import deque
def bfs(graph, start, visited):
    # 시작 노드 방문처리
    queue = deque([start])
    visited[start] = True
    while(queue):
        v = queue.popleft()
        print(v, end=" ")
        for node in graph[v]: # 인접 노드 반복
            if not visited[node]:
                queue.append(node) # 스택에 추가
                visited[node] = True # 방문처리


from sys import stdin
input = stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    node1, node2 = list(map(int, input().split()))
    graph[node1].append(node2)
    graph[node2].append(node1)

for nodes in graph:
    nodes.sort()

visited = [False] * len(graph)
dfs(graph, v, visited)
print()
visited = [False] * len(graph)
bfs(graph, v, visited)