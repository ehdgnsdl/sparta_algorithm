from collections import deque

game_map = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "B", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", "R", "O", ".", "#"],
    ["#", "#", "#", "#", "#"],
]
#     북  동  남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


# 방문 저장 여부 visitied 를 만들어야 하는데
# 공이 2개??? 어떻게 해야 방문하는지 아닌지를 알 수 있을까요?
# 4차원 배열을 사용하면 됩니다.
#                n                m                n                m
# visited[red_marble_row][red_marble_col][blue_marble_row][blue_marble_col]
# 3 <= x <= 10
# [[
# [
#   [False, False, False, False, False],
#   [False, False, False, False, False],
#   [False, False, False, False, False],
#   [False, False, False, False, False],
#   [False, False, False, False, False]
#  ], [
#  [False, False, False, False, False],
#  [False, False, False, False, False],
#  [False, False, False, False, False],
#  [False, False, False, False, False],
#  [False, False, False, False, False]
#  ], [
#  [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False]], [[False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False]], [[False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False]]], [[[False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False]], [[False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False]], [[False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False]], [[False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False]], [[False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False]]], [[[False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False]], [[False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False]], [[False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False]], [[False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False]], [[False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False]]], [[[False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False]], [[False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False]], [[False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False]], [[False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False]], [[False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False]]], [[[False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False]], [[False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False]], [[False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False]], [[False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False]], [[False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False]]]]

def move_until_wall_or_hole(r, c, diff_r, diff_c, game_map):
    move_count = 0 # 이동한 칸 수
    # 다음 이동이 벽이거나 구멍이 아닐 때까지
    while game_map[r + diff_r][c + diff_c] != "#" and game_map[r][c] != "O":
        r += diff_r
        c += diff_c
        move_count += 1
    return r, c, move_count


def is_available_to_take_out_only_red_marble(game_map):
    n, m = len(game_map), len(game_map[0])  # 행과 열의 크기 (5, 5)
    visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    red_row, red_col, blue_row, blue_col = -1, -1, -1, -1
    queue = deque() # 탐색 횟수까지 큐에 넣어준다.
    # 빨간 구슬과 파란 구슬의 위치를 이중 반복문을 이용해서 찾아준다.
    for i in range(n):
        for j in range(m):
            if game_map[i][j] == "R":
                red_row, red_col = i, j
            elif game_map[i][j] == "B":
                blue_row, blue_col = i, j
    # 탐색을 10번까지만 할 수 있다.
    queue.append((red_row, red_col, blue_row, blue_col, 1))
    visited[red_row][red_col][blue_row][blue_col] = True

    while queue:
        red_row, red_col, blue_row, blue_col, try_count = queue.popleft()
        if try_count > 10:
            break

        for i in range(4):
            next_red_row, next_red_col, r_count = move_until_wall_or_hole(red_row, red_col, dr[i], dc[i], game_map)
            next_blue_row, next_blue_col, b_count = move_until_wall_or_hole(blue_row, blue_col, dr[i], dc[i], game_map)

            if game_map[next_blue_row][next_blue_col] == 'O': # 파란 구슬이 구멍에 떨어지지 않으면(실패 X)
                continue
            if game_map[next_red_row][next_red_col] == 'O': # 빨간 구슬이 구멍에 떨어진다면 (성공)
                return True
            # 빨간 구슬과 파란 구슬이 동시에 같은 칸에 있을 수 없다.
            if next_red_row == next_blue_row and next_red_col == next_blue_col: # 빨간 구슬과 파란 구슬이 동시에 같은 칸에 있을 수 없다.
                if r_count > b_count: # 이동거리가 많은 구슬을 한칸 뒤로
                    next_red_row -= dr[i]
                    next_red_col -= dc[i]
                else:
                    next_blue_row -= dr[i]
                    next_blue_col -= dc[i]
            # BFS 탐색을 마치고, 방문 여부 확인
            if not visited[next_red_row][next_red_col][next_blue_row][next_blue_col]:
                visited[next_red_row][next_red_col][next_blue_row][next_blue_col]=True
                queue.append((next_red_row, next_red_col, next_blue_row, next_blue_col, try_count + 1))

    # 구현해보세요!
    return False


print(is_available_to_take_out_only_red_marble(game_map))  # True 를 반환해야 합니다
