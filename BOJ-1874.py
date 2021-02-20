from sys import stdin

input = stdin.readline
n = int(input())
series = [int(input()) for _ in range(n)]

stack = []
result = ""
num = 1
for s in series:
    # 수열의 값과 같아질때까지 증가하며 스택에 push
    while num <= s:
        stack.append(num)
        result += '+\n'
        num += 1
        
    # 스택의 마지막 값과 같은 경우
    if stack.pop() == s:
        result += '-\n'
    # 스택의 마지막 값과 다르면 수열만들기 불가능함
    else:
        result = "NO\n"
        break

print(result, end="")