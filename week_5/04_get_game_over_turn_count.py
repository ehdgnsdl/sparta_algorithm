k = 4  # 말의 개수

chess_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
start_horse_location_and_directions = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 2, 0],
    [2, 2, 2]
]
# 이 경우는 게임이 끝나지 않아 -1 을 반환해야 합니다!
# 동 서 북 남
# →, ←, ↑, ↓
dr = [0, 0, -1, 1] # row
dc = [1, -1, 0, 0] # columns
# 0 -> 1
# 1 -> 0
# 2 -> 3
# 3 -> 2
def get_d_index_when_go_back(d):
    if d % 2 ==0:
        return d+1
    else:
        return d-1


# 말은 순서대로 이동하빈다 -> 말의 순서에 따라 반복문
# 말이 쌓일 수 있습니다. -> 맵에 말이 쌓이는걸 저장해놔야 합니다.
# 쌓인 순서대로 이동합니다 -> stack 써야겠구나.
# 현재 맵에 어떻게 말이 쌓이지를 저장하기 위해서는
# chess_map
# [
#     [[0], [1], [2], []],
#     [[], [], [], []],
#     [[], [], [3], []],
#     [[], [], [], []]
# ] -> current_stacked_horse_map

# 강의 한번 더 봐야할듯.
def get_game_over_turn_count(horse_count, game_map, horse_location_and_directions):
    n = len(chess_map)
    current_stacked_horse_map = [ # 현재 말들이 쌓여있는 것을 저장하는 것 linked list
        [
            [] for _ in range(n)
        ] for _ in range(n)
    ] # 3차원 배열의 구성이구나.

    for i in range(horse_count): # 현재 말들이 들어간 위치?
        r, c, d = horse_location_and_directions[i] # row, columns, 이동방향
        current_stacked_horse_map[r][c].append(i)
    turn_count = 1

    while turn_count <= 1000:
        for horse_index in range(horse_count):
            r, c, d = horse_location_and_directions[horse_index] 
            new_r = r + dr[d] # 위치가 변경되는 것을 구현
            new_c = c + dc[d]

            # 파란색이거나 맵을 나갔을 때, (맨 마지막에 구현했음.)
            if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                new_d = get_d_index_when_go_back(d) # 새로운 방향을 얻음.

                # 0, 1, 2가 r, c, d 순
                horse_location_and_directions[horse_index][2] = new_d
                new_r = r+dr[new_d]
                new_c = c+dc[new_d]
                # 가기로한 곳이 막혀 있으면 안감.
                if not 0 <= new_r < n or not 0 <= new_c < n or game_map[new_r][new_c] == 2:
                    continue


            # 2가 이동한다고 치면 2, 3만 이동
            # 즉, 자기 자신의 인덱습돠 큰 애들만 데리고갑니다.
            # [1 2 3] [:i]

            moving_horse_index_array = [] # 이동할 애들만 넣어주는 배열
            # 이동할 애들 부분 구현
            for i in range(len(current_stacked_horse_map[r][c])): # index를 사용해야 하기 때문에
                current_stacked_horse_index = current_stacked_horse_map[r][c][i] # i는 쌓여져 있는 말의 인덱스 번호
                if horse_index == current_stacked_horse_index:
                    moving_horse_index_array = current_stacked_horse_map[r][c][i:] # 이동하는 애들
                    current_stacked_horse_map[r][c] = current_stacked_horse_map[r][c][:i] # 남는 애들
                    break
            if game_map[new_r][new_c] == 1:
                moving_horse_index_array = reversed(moving_horse_index_array)


            # 말들을 새로운 위치로 옮김
            for moving_horse_index in moving_horse_index_array:
                current_stacked_horse_map[new_r][new_c].append(moving_horse_index)
                horse_location_and_directions[moving_horse_index][0], horse_location_and_directions[moving_horse_index][1] = new_r, new_c

            # 턴이 진행되는 중 말이 4개 이상 쌓이는 순간 게임이 종료된다. (탈출조건. 맨마지막에 구현)
            if len(current_stacked_horse_map[new_r][new_c]) >=4:
                return turn_count
        turn_count += 1

    return -1


print(get_game_over_turn_count(k, chess_map, start_horse_location_and_directions))  # 2가 반환 되어야합니다