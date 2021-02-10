from sys import stdin
input = stdin.readline

n = int(input())
deque = []
for _ in range(n):
    command = input().strip()
    if 'push_front' in command:
        deque.insert(0, command.split()[1])
    elif 'push_back' in command:
        deque.append(command.split()[1])
    elif command == 'pop_front':
        if deque:
            print(deque.pop(0))
        else:
            print(-1)
    elif command == 'pop_back':
        if deque:
            print(deque.pop())
        else:
            print(-1)
    elif command == 'size':
        print(len(deque))
    elif command == 'empty':
        if deque:
            print(0)
        else:
            print(1)
    elif command == 'front':
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif command == 'back':
        if deque:
            print(deque[-1])
        else:
            print(-1)
        