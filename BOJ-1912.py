# BOJ-1912.py
# 연속합

from sys import stdin
input = stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

total = numbers[0]
max_total = total
for i in range(1, n):
    total = max(total + numbers[i], numbers[i])
    max_total = max(max_total, total)
    
print(max_total)

