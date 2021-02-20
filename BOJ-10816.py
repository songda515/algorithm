from sys import stdin
from collections import Counter

input = stdin.readline

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
finds = list(map(int, input().split()))

count = Counter(nums) # dictionary
result = []
for f in finds:
    result.append(count[f])

print(" ".join(map(str, result)))