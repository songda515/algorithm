# programmers H-index.py

"""
H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다.
어떤 과학자가 발표한 논문 n편 중, 
    h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 
    h의 최댓값이 이 과학자의 H-Index입니다.
citations: 어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열
return : 이 과학자의 H-Index
"""

def solution(citations):
    h_list = [0]
    for h in range(max(citations)):
        if h > 1000:
            break
        # more : h 번 이상 인용된 논문의 개수
        # rest : h 번 이하 인용된 논문의 리스트
        more = 0
        rest = [0]
        for x in citations:
            if x >= h:
                more += 1
            else:
                rest.append(x)

        # more 중 h 번 이상 인용된 논문이 h개 이상인지?
        # 나머지 논문이 h번 이하 인용되었는지?        
        if more >= h and max(rest) <= h:
            h_list.append(h)
    return max(h_list)    

print(solution([3, 0, 6, 1, 5])) # return 3
