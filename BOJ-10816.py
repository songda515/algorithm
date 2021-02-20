from sys import stdin
from bisect import bisect_left, bisect_right

input = stdin.readline
def count(array, num):
    left = bisect_left(array, num)
    right = bisect_right(array, num)
    return right - left

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
finds = list(map(int, input().split()))

nums.sort()
result = []
for f in finds:
    result.append(count(nums, f))

print(" ".join(map(str, result)))