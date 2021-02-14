from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
a, b, d = map(int, input().split())

game_map = []
for _ in range(n):
    # 0 육지 1 바다
    game_map.append(list(map(int, input().split())))

# 0 북 1 동 2 남 3 서 
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def rotate_dir(d):
    if d == 0:
        return 3
    return d - 1

count = 1
d_count = 0
while(True):
    d_count += 1
    # 네 방향 전부 못가는 경우
    if d_count == 4:
        dd = rotate_dir(rotate_dir(d)) # 뒤쪽 방향
        y, x = a + dy[dd], b + dx[dd]
        # 뒤쪽 방향이 바다인 경우
        if game_map[y][x] == 1:
            break
        # 뒤로 한 칸 이동
        else:
            a, b = y, x
            d_count = 0
            continue

    d = rotate_dir(d)
    y, x = a + dy[d], b + dx[d]
    print("a, b >", a, b, ">> y, x >", y, x)
    # 이동할 수 있는 경우
    if game_map[y][x] == 0:
        game_map[y][x] = 2
        a, b = y, x
        d_count = 0
        count += 1
    # 이동할 수 없는 경우
    else:
        continue

print(count)