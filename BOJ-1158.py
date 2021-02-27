# BOJ-1158.py

from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
nums = list(range(1, n+1))
index = k - 1
result = []
while(True):
    result.append(nums.pop(index))
    if not nums:
        break
    index += k - 1
    if index >= len(nums):
        index = index % len(nums)

print("<{}>".format(", ".join(map(str, result))))