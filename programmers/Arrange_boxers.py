def solution(weights, head2head):
    answer = list()
    win_rate = list()
    # 복서 승률 계산, 이긴횟수 세기(나보다 무거운 사람), 자신의 무게, 자신의 번호 넣기
    for i, (w, head) in enumerate(zip(weights, head2head)):
        win_count = 0 #무거운 사람을 이긴 사람 횟수
        win = 0
        lose = 0
        for j, h in enumerate(head):
            if h == "W":
                win += 1
                if w < weights[j]:
                    win_count += 1
            if h == "L": lose += 1
        if win == 0 or (win + lose) == 0:
            rate = 0
        else:
            rate = win / (win + lose)
            win_rate.append((rate, win_count, w, i + 1))
    # 승률 높은 사람, 이긴 횟수가 많은 사람, 자신의 무게가 무거운 사람, 자기 번호가 낮은 사람 기준 정렬
    win_rate.sort(key=lambda x: (-x[0], -x[1], -x[2], x[3]))
    return [num for w, w1, w3, num in win_rate]

