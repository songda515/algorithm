# programmers_func_dev.py
# 스택/큐 - 기능개발

"""
progresses : 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열
speeds : 각 작업의 개발 속도가 적힌 정수 배열
return : 각 배포마다 몇 개의 기능이 배포되는지
"""

def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    while len(progresses) > 0:
        print(progresses, speeds, answer, time)
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer


print(solution([93, 30, 55], [1, 30, 5])) # return [2, 1]
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])) # return [1, 3, 2]