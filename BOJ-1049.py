from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
set_prices = [0] * m
one_prices = [0] * m
for i in range(m):
    set_prices[i], one_prices[i] = map(int, input().split())

money = 0
while(n >= 6):
    n = n - 6
    if min(set_prices) > min(one_prices) * 6:
        money += min(one_prices) * 6
    else:
        money += min(set_prices)

if min(set_prices) > min(one_prices) * n:
    money += min(one_prices) * n
else:
    money += min(set_prices)

print(money)