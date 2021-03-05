# programmers_printer

"""
들어온 순서대로 인쇄 -> First In First Out -> Stack
중요도가 높은 문서를 먼저 인쇄 -> 우선순위 Stack
1. 가장 앞에 있는 문서 J 꺼냄
2. 나머지 인쇄 목록 중 J 보다 중요도가 높으면 J 를 대기목록의 마지막에 삽입
3. 그렇지 않으면 J 를 인쇄
"""

from collections import deque

# priorities : 현재 대기목록에 있는 문서의 중요도가 순서대로 담긴 배열
# location : 내가 인쇄를 요청한 문서가 현재 대기목록의 어떤 위치에 있는지
# return : 내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지
def solution(priorities, location):
    queue = deque(range(len(priorities)))
    count = 0

    while(queue):
        # 가장 앞에 있는 문서 J 를 꺼냄
        j = queue.popleft()
        
        for i in queue:
            if j == i: 
                pass
            # J 보다 중요도가 높은 게 있다면 J 를 마지막으로
            if priorities[j] < priorities[i]:
                queue.append(j)
                break
        
        # j 가 스택에 없다면 리턴된것
        if not j in queue:
            count += 1
            # j 가 찾는 값이라면 반복 종료 
            if j == location:
                break
    return count


print(solution([2, 1, 3, 2], 2)) # case 1 : return 1
print(solution([1, 1, 9, 1, 1, 1], 0)) # case 2 : return 5