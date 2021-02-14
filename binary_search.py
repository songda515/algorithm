from sys import stdin
from bisect import bisect_left, bisect_right
input = stdin.readline

n = int(input())
parts = list(map(int, input().split()))
parts.sort()

m = int(input())
requests = list(map(int, input().split()))

for r in requests:
    left = bisect_left(parts, r)
    right = bisect_right(parts, r)
    # index 가 같으면 해당 원소가 없는 것
    if left == right:
        print("no")
    else:
        print("yes")
    