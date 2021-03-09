# programmers _ pratice exam.py

def solution(answers):
    person = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    count = [0] * 3

    for i, answer in enumerate(answers):
        for p in range(3):
            l = len(person[p])
            if person[p][i % l] == answer:
                count[p] += 1

    max_person = []
    max_count = max(count)
    for i, c in enumerate(count):
        if c == max_count:
            max_person.append(i+1)

    return max_person


print(solution([1,2,3,4,5])) # [1]
print(solution([1,3,2,4,2])) # [1,2,3]
