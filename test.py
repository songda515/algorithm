# 18110
from sys import stdin
input = stdin.readline

def new_round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

n = int(input()) # stdin.readline()
if n == 0:
    print(0)
else:
    # levels = []
    # for i in range(n):
    #     levels.append(int(input())
    levels = [int(input()) for i in range(n)]
    levels.sort()
    x = new_round(n * 0.15)
    result = new_round(sum(levels[x: n-x]) / (n-2*x))
    print(result)