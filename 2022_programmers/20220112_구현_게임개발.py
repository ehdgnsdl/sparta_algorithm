# N,  M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

# 맵을 생성. n X m 맵
d = [[0] * m for _ in range(n)]

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 캐릭터 x, y좌표 및 바라보는 방향
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리함

# 바다(1)와 육지(0) 생성
array = []
for i in range(n):
    array.append(list(map(int, input().split())))


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


# 방문 횟수
count = 1
# 왼쪽으로 돈 횟수
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 돌았을 때, 육지가 있으면서 맵이 있다면
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 돌았을 때, 바다면서 맵이 없다면
    else:
        turn_time += 1
    # 왼쪽으로 총 4번 돌았다면 (더이상 이동할 곳이 없다면)
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면
        if array[nx][ny] == 0:
            x = nx
            y = ny
            turn_time = 0
        # 뒤로 갈 수 없다면(바다로 막혀있다면)
        else:
            break

print(count)
