# BOJ-1912.py
# 연속합

from sys import stdin
input = stdin.readline

n = int(input())
numbers = list(map(int, input().split()))

max_sum = -1000
dp = [0] * 100001
for i in range(n):
    dp[i] = max(dp[i-1] + numbers[i], numbers[i])
    max_sum = max(max_sum, dp[i])
    
print(max_sum)

