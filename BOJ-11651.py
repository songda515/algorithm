from sys import stdin
input = stdin.readline

n = int(input())
coords = []
for _ in range(n):
    coords.append(list(map(int, input().split())))

# 정렬하는 기준 y축 오름차순 -> x축 오름차순
coords = sorted(coords, key= lambda coord: (coord[1], coord[0]))
for coord in coords:
    print(coord[0], coord[1])