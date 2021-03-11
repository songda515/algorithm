# BOJ-1697.py
# 숨바꼭질

# X -> X-1 or X+1 or 2*X
from collections import deque
def bfs(v, k, time):
    queue = deque([v])
    while(queue):
        v = queue.popleft()
        if v == k:
            return time[v]
        for next_step in (v-1, v+1, v*2):
            if 0 <= next_step < MAX and not time[next_step]:
                time[next_step] = time[v] + 1
                queue.append(next_step)

from sys import stdin
input = stdin.readline
n, k = map(int, input().split())

MAX = 100001
time = [0] * MAX
print(bfs(n, k, time))