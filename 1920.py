# 1920
from sys import stdin
input = stdin.readline

def binary_search(array, target):
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if target == array[mid]:
            return 1
        elif target > array[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0

n = int(input())
a = list(map(int, input().split()))
a.sort()
m = int(input())
x = list(map(int, input().split()))

#print(a, x)
for i in x:
    print(binary_search(a, i))