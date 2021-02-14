from sys import stdin
input = stdin.readline

n = int(input())
for _ in range(n):
    string = input()
    stack = 0
    for s in string:
        if s == '(':
            stack += 1
        elif s == ')':
            stack -= 1
            if stack < 0:
                break
    if stack == 0:
        print("YES")
    else:
        print("NO")