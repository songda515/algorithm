from sys import stdin
input = stdin.readline

n = int(input())
words = set()
for _ in range(n):
    words.add(input().strip())

words = sorted(words, key=lambda x: (len(x), x))
print('\n'.join(map(str, words)))