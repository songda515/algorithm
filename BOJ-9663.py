# BOJ-9663.py
# N-Queen

from sys import stdin
input = stdin.readline

n = int(input())
answer = 0
a, b, c = [False]*n, [False]*(2*n-1), [False]*(2*n-1)

def dfs(y):
    global answer
    if y == n:
        answer += 1
        return
    for x in range(n):
        if not (a[x] or b[y+x] or c[y-x+n-1]):
            a[x] = b[y+x] = c[y-x+n-1] = True
            dfs(y+1)
            a[x] = b[y+x] = c[y-x+n-1] = False

dfs(0)
print(answer)