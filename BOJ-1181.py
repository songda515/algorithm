from sys import stdin
input = stdin.readline

n = int(input())
words = {}
for _ in range(n):
    words[input().strip()] = 0

words = sorted(words.keys(), key=lambda x: (len(x), x))
print('\n'.join(map(str, words)))