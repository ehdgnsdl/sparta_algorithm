# 현재 나이트의 위치 입력 받기
input_data = input()
row = int(input_data[1])
# ord()는 문자를 숫자로 바꿔주는 것
columns = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-2, 1), (-1, 2), (-1, -2),
         (1, 2), (1, -2), (2, 1), (2, -1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한 지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = columns + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if 1 <= next_row <= 8 and 1 <= next_column <= 8:
        result += 1
print(result)