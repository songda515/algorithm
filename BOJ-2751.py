from sys import stdin
input = stdin.readline

n = int(input())
array = [int(input()) for _ in range(n)]
array.sort()
print('\n'.join(map(str, array)))