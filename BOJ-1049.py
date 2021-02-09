from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
set_price = one_price = 1000
for i in range(m):
    s, o = map(int, input().split())
    set_price = min(s, set_price)
    one_price = min(o, one_price)

money = (n // 6) * min(set_price, one_price * 6)
money += min(set_price, one_price * (n % 6))
print(money)