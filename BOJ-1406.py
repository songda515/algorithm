from sys import stdin
input = stdin.readline

left = list(input().strip())
right = list()
m = int(input())

for _ in range(m):
    command = input().strip()
    if command == 'L' and left:
        right.append(left.pop())
    elif command == 'D' and right:
        left.append(right.pop())
    elif command == 'B' and left:
        left.pop()
    elif 'P' in command:
        left.append(command.split()[1])

right.reverse()
print(''.join(left + right))