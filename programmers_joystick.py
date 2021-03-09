# programmers_joystick.py

"""
조이스틱으로 알파벳 이름을 완성하세요.
맨 처음엔 A로만 이루어져 있습니다.
- name : 만들고자 하는 이름
- return : 조이스틱 조작 횟수의 최솟값
"""

UP, DOWN = 1, 0
count = 0

def rotate(alphabet, direction):
    global UP, DOWN
    if direction == UP:
        if alphabet == 'Z':
            return 'A'
        else:
            next_alphabet = ord(alphabet) + 1
            return chr(next_alphabet)
    elif direction == DOWN:
        if alphabet == 'A':
            return 'Z'
        else:
            next_alphabet = ord(alphabet) - 1
            return chr(next_alphabet)

def replace(joy_name, name):
    global UP, DOWN, count
    if abs(ord(joy_name) - ord(name)) < 13:
        while(joy_name != name):
            joy_name = rotate(joy_name, UP)
            count += 1
    else:
        while(joy_name != name):
            joy_name = rotate(joy_name, DOWN)
            count += 1
    return joy_name

def solution2(name):
    global UP, DOWN, count
    joy_name = ["A"] * len(name)
    name = list(name)
    count, index = 0, 0
    direction = UP # UP = RIGHT, DOWN = LEFT

    joy_name[index] = replace(joy_name[index], name[index])
    while(joy_name != name):
        if index == 0 and name[index + 1] == 'A':
            index = len(name) - 1
            direction = DOWN
        elif direction == UP:
            index += 1
        elif direction == DOWN:
            index -= 1

        count += 1
        joy_name[index] = replace(joy_name[index], name[index]) 
        print(joy_name, count, index)

    return count


solution("JAZ") # return 11
#solution("JAN") # return 23
#solution("JEROEN") # return 56
#solution("BBBAAAB")
#solution("BBAABAAAAB")