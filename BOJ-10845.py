from sys import stdin
input = stdin.readline

n = int(input())
queue = []
for _ in range(n):
    command = input().strip()
    if command == 'pop':
        if queue:
            print(queue.pop(0))
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
    else:
        queue.append(command.split()[-1])