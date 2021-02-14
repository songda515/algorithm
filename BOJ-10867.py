from sys import stdin
input = stdin.readline

n = int(input())
num = set(map(int, input().split()))
num = list(num)
num.sort()
print(" ".join(map(str, num)))