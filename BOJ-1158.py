# BOJ-1158.py

from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
nums = list(range(1, n+1))
index = k - 1
result = []
for _ in range(n):
    index = index % len(nums)    
    result.append(nums.pop(index))
    index += k - 1

print("<{}>".format(", ".join(map(str, result))))