from sys import stdin
input = stdin.readline

n = int(input())
num = list(map(int, input().split()))
count = [0] * 2003
for n in num:
    count[n+1001] += 1

for i, c in enumerate(count):
    if c > 0:
        print(i-1001, end=" ") 