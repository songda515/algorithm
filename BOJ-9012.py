from sys import stdin
input = stdin.readline

n = int(input())
strings = []
for _ in range(n):
    strings.append(input()) 

for string in strings:
    is_valid = True
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif s == ')':
            if stack:
                stack.pop()
            else:
                is_valid = False
                break
    if not stack and is_valid:
        print("YES")
    else:
        print("NO")
