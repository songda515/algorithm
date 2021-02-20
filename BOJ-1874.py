from sys import stdin
from bisect import bisect_left, bisect_right
input = stdin.readline

def is_in(array, target):
    left = bisect_left(array, target)
    right = bisect_right(array, target)
    if left == right:
        return False
    return True

n = int(input())
series = []
for _ in range(n):
    series.append(int(input()))

stack = []
series_stack =[]
num = range(1, n+1)
i = -1
result = []
for s in series:
    while i < n:
        # 이미 스택에 있는 경우
        #if s in stack:
        if is_in(stack, s):
            item = stack.pop()
            if item == s:
                #print(s, num[i], "-", item)
                result.append("-")
                series_stack.append(item)
                break
            else:
                result = ["NO"]
                i = n
                break
        i += 1
        if s > num[i]:
            #print(s, num[i], "+")
            result.append("+")
            stack.append(num[i])
        if s == num[i]:
            #print(s, num[i], "+")
            result.append("+")
            stack.append(num[i])
            #print(s, num[i], "-")
            result.append("-")
            series_stack.append(stack.pop())
            break
        if s < num[i]:
            #print(s, num[i], "-")
            result.append("-")
            series_stack.append(stack.pop())

    #print(stack, series_stack)

print("\n".join(result))