# programmers_위장.py

"""
clothes : 스파이가 가진 의상들이 담긴 2차원 배열
return : 서로 다른 옷의 조합의 수
"""

from itertools import product

def solution(clothes):
    # Key: 종류, Value: 이름 으로 Dictionary 만들기 
    clothes_dict = {}
    for c in clothes:
        key = c[1]
        if not key in clothes_dict:
            clothes_dict[key] = [0]
        clothes_dict[key].append(c[0])
    
    #print(list(product(*clothes_dict.values())))
    combination = len(list(product(*clothes_dict.values()))) - 1
    return combination


# return 5
result = solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]])
print(result)
# return 3
result = solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]])
print(result)

# return 63
print(solution([
["a","aa"],
["b","aa"],
["c","aa"],
["aa","bb"],
["bb","bb"],
["c_c","bb"],
["aaa","cc"],
["bbb","cc"],
["ccc","cc"]
]))

# return 7
print(solution([
["a", "a"], 
["b", "b"], 
["c", "c"]
]))

# a, b, c, a+b, a+c, b+c, a+b+c