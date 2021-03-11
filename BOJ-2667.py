# BOJ-2667.py 
# 단지 번호 붙이기

def dfs(x, y, n, graph, location, count):
    if x <= -1 or y <= -1 or x >= n or y >= n:
        return False

    if graph[x][y] == '1' and location[x][y] == 0:
        location[x][y] = count
        dfs(x, y-1, n, graph, location, count)
        dfs(x, y+1, n, graph, location, count)
        dfs(x-1, y, n, graph, location, count)
        dfs(x+1, y, n, graph, location, count)
        return True
    return False


from sys import stdin
input = stdin.readline

n = int(input())
graph = []
location = []
for _ in range(n):
    graph.append(input().strip())
    location.append([0] * n)

count = 1
for x in range(n):
    for y in range(n):
        if dfs(x, y, n, graph, location, count):
            count += 1

location_flat = sum(location, [])
max_count = max(location_flat)
print(max_count)
location_count = []
for i in range(1, max_count+1):
    location_count.append(location_flat.count(i))

location_count.sort()
print("\n".join(map(str, location_count)))