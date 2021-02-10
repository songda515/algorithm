from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
queue = deque()
for _ in range(n):
    command = input().strip()
    if 'push_front' in command:
        queue.appendleft(command.split()[1])
    elif 'push_back' in command:
        queue.append(command.split()[1])
    elif command == 'pop_front':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif command == 'pop_back':
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif command == 'size':
        print(len(queue))
    elif command == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif command == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
        