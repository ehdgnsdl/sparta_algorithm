from collections import deque

c = 11
b = 2


# 브라운의 위치 변화는
# B - 1, B + 1, 2 * B 중에 하나.

# 모든 경우의 수를 다 나열해야겠구나
# BFS를 써야겠꾸나.

# 잡았다!라는 의미는 똑같은 시간에 똑같은 위치에 존재햐아합니다.
# 시간은 + 1
# 위치 코니도 브라운도 값이 자유자재로 바뀜.
#
# 규칙적 -> 배열, 자유자재 -> 딕셔너리
#
# 각 시간마다 브라운이 갈 수 있는 위치를 저장하고 싶음
# 브라운과 코니의 위치를 구하자.
def catch_me(cony_loc, brown_loc):
    time = 0
    queue = deque()
    queue.append((brown_loc, 0))  # 위치와 시간
    visited = [{} for _ in range(200001)]
    # visited[위치][시간]
    # visited[3] 에 5라는 키가 있냐? 라고하면 3 위치에 5초에 간 적이 있냐?
    # 시간 0   1   2 -> visited[2] = {0: True, 2: True}
    # 위치 2 ->1   0 -> visited[1] = {1: True}
    #         3   2 -> visited[3] = {1: True}
    #         4   3 -> visited[4] = {1: True}
    #             4
    #             8
    while cony_loc <= 20000:
        cony_loc += time  # 시간만큼 +1 +2 +3 +4
        if time in visited[cony_loc]:
            return time

        for i in range(0, len(queue)):
            current_position, current_time = queue.popleft()

            new_time = current_time + 1
            new_position = current_position - 1
            if 0 <= new_position <= 200000:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position + 1
            if 0 <= new_position <= 200000:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))

            new_position = current_position * 2
            if 0 <= new_position <= 200000:
                visited[new_position][new_time] = True
                queue.append((new_position, new_time))
        time += 1
    return -1


print(catch_me(c, b))  # 5가 나와야 합니다!
