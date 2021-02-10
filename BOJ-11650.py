from sys import stdin
input = stdin.readline

n = int(input())
point_dict = {}

for _ in range(n):
    x, y = map(int, input().split())
    if not x in point_dict.keys():
        point_dict[x] = []
    point_dict[x].append(y)

for x in sorted(point_dict.keys()):
    for y in sorted(point_dict[x]):
        print(x, y)