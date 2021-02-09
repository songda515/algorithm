from sys import stdin
input = stdin.readline
n = int(input())
count = [0] * 10001
for _ in range(n):
    a = int(input())
    count[a] += 1

for i in range(1, 10001):
    print(f"{i}\n" * count[i], end='')