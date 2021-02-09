from sys import stdin
input = stdin.readline

t = int(input())
for _ in range(t):
    c, v = map(int, input().split())
    preference = []
    first = {}
    second = {}
    # 입력 
    for _ in range(v):
        preference.append(list(map(int, input().split())))

    # 초기화
    for i in range(1, c+1):
        first[i] = 0

    # 1회차
    for p in preference:
        first[p[0]] += 1

    max_index = max(first.keys(), key= lambda x: first[x])
    if first[max_index] > v // 2:
        print(max_index, 1)
    else:
        # 2회차
        remains = sorted(first.items(), key= lambda x: x[1], reverse=True)
        print(remains)
        for i in range(2):
            second[remains[i][0]] = 0
        print(second)
        for pp in preference:
            for p in pp:
                if p == list(second.keys())[0] or p == list(second.keys())[1]:
                    second[p] += 1
                    break
        
        max_index = max(second.keys(), key= lambda x: second[x])
        print(max_index, 2)
