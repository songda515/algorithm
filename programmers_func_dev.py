# programmers_func_dev.py
# 스택/큐 - 기능개발

"""
progresses : 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열
speeds : 각 작업의 개발 속도가 적힌 정수 배열
return : 각 배포마다 몇 개의 기능이 배포되는지
"""

def solution(progresses, speeds):
    count = []
    distribute = [0] * len(progresses)
    current = 0
    while(min(distribute) == 0):
        for i, progress in enumerate(progresses):
            if progress >= 100 and distribute[i] == 0:
                distribute[i] = 1
            else:
                progresses[i] += speeds[i]

        if 1 in distribute:        
            found = distribute.index(1)
            if current == found:
                c = 0
                for i in range(current, len(distribute)):
                    if distribute[i] == 0:
                        break # 중간에 배포안된 부분
                    if distribute[i] == 1:
                        c += 1
                        distribute[i] = 2
                count.append(c)
                current += c

        print("\n", progresses, speeds, distribute, count)
    return count

#print(solution([93, 30, 55], [1, 30, 5])) # return [2, 1]
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])) # return [1, 3, 2]