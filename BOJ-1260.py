# BOJ-1260.py

# DFS (Depth First Search)
# DFS 는 stack 자료구조 혹은 재귀함수를 이용한다.
def dfs(graph, v, visited):
    # 현재 노드 방문처리
    visited[v] = True
    print(v, end=" ")
    # 인접 노드 반복 
    for node in graph[v]:
        # 인접 노드 중 방문하지 않은 노드에 대해 DFS 수행
        if not visited[node]:
            dfs(graph, node, visited)


# BFS (Breath First Search)
# BFS 는 queue 자료구조를 이용한다.
from collections import deque
def bfs(graph, start, visited):
    queue = deque([start])
    # 현재 노드 방문처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while(queue):
        # 큐에서 원소를 하나 뽑기 -> 현재 노드
        v = queue.popleft()
        print(v, end=" ")
        # 인접 노드 반복
        for node in graph[v]:
            # 인접 노드 중 방문하지 않은 노드 queue 에 추가 & 방문처리
            if not visited[node]:
                queue.append(node)
                visited[node] = True


from sys import stdin
input = stdin.readline

n, m, v = map(int, input().split())
graph = [0]
for i in range(n):
    graph.append([])

for _ in range(m):
    node1, node2 = list(map(int, input().split()))
    graph[node1].append(node2)
    graph[node2].append(node1)

for i in range(1, n+1):
    graph[i] = sorted(graph[i])

visited = [False] * (n+1)
dfs(graph, v, visited)
print()
visited = [False] * (n+1)
bfs(graph, v, visited)