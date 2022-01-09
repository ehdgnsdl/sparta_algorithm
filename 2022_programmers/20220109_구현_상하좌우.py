# N을 입력 받기 aa
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
# 이동 방향을 설정.
for plan in plans:
    # 이동 후 좌표 구하기
    # 인덱스로 접근해야함. dx와 dy를 인덱스로 표현했기 때문에,
    for i in range(len(move_types)):        
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시(5 X 5이므로)
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny
    
print(x, y)
