from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
queue = deque()
for _ in range(n):
    cmd = input().strip()
    if cmd == 'pop_front':
        if len(queue) > 0:
            print(queue.popleft())
        else:
            print(-1)
    elif cmd == 'pop_back':
        if len(queue) > 0:
            print(queue.pop())
        else:
            print(-1)
    elif cmd == 'size':
        print(len(queue))
    elif cmd == 'empty':
        if len(queue) > 0:
            print(0)
        else:
            print(1)
    elif cmd == 'front':
        if len(queue) > 0:
            print(queue[0])
        else:
            print(-1)
    elif cmd == 'back':
        if len(queue) > 0:
            print(queue[-1])
        else:
            print(-1)
    else:
        cmd = cmd.split()
        if cmd[0] == 'push_front':
            queue.appendleft(cmd[1])
        elif cmd[0] == 'push_back':
            queue.append(cmd[1])
            
    print(queue)
        