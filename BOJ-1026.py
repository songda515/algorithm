from sys import stdin
input = stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse=True)
s = list(map(lambda x: a[x]*b[x], range(n)))
print(sum(s))