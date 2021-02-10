from sys import stdin
input = stdin.readline

n = int(input())
points = []

for _ in range(n):
    points.append(list(map(int, input().split())))

points = sorted(points, key = lambda point: (point[0], point[1]))

for p in points:
    print(p[0], p[1])