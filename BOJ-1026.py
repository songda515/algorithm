from sys import stdin
input = stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def min_sort(a, b, n):
    indexs = list(range(n))
    # 선택 정렬 - b 배열과 b배열의 index
    for i in range(n):
        max_index = i
        for j in range(i+1, n):
            if b[j] > b[max_index]:
                max_index = j
        b[i], b[max_index] = b[max_index], b[i]
        indexs[i], indexs[max_index] = indexs[max_index], indexs[i]

    # a 배열의 index 재정렬
    a.sort()
    result = [0] * n
    for i in range(n):
        result[indexs[i]] = a[i]
    return result

a = min_sort(a, b.copy(), n)
s = list(map(lambda x: a[x]*b[x], range(n)))
print(sum(s))