# programmers - target number.py
# 깊이/너비 우선 탐색(DFS/BFS)

"""
numbers : 사용할 수 있는 숫자가 담긴 배열
target : 타겟 넘버
return : 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수
"""

from itertools import product

def solution(numbers, target):
    length = len(numbers)
    # 전체 가능한 case 
    cases = []
    for _ in range(length):
        cases.append([-1, 1])
    cases = list(product(*cases))
    #print(len(cases))

    count = 0
    for case in cases:
        s = 0
        for i in range(length):
            s += case[i] * numbers[i]
        if s == target:
            count += 1
    return count

print(solution([1, 1, 1, 1, 1], 3))