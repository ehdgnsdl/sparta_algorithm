n = 5
lost = [2, 4]
reserve = [1, 3, 5]


def solution(n, lost, reserve):
    answer = 0
    # 도난당한거 방지. 집합으로 만듦
    set_reserve = set(reserve)-set(lost)
    set_lost = set(lost)-set(reserve)

    # set_reserve를 기준으로
    # 기준을 set_lost하면 안되는 이유는. set_lost는 dictionary인데, set_lost.remove()로 딕셔너리를 변경시키면서 for문을 못돌기 때문이다.
    # 그래서 set_reserve 기준으로 for문을 돌린 후에 dictionary인 set_lost를 remove()해준다.
    for i in set_reserve:
        # i-1이 set_lost에 있다면 set_lost(i-1)을 제거
        if i-1 in set_lost:
            set_lost.remove(i-1)
        # i+1이 set_lost에 있다면 set_lost(i+1)을 제거
        elif i+1 in set_lost:
            set_lost.remove(i+1)

    answer = n - len(set_lost)

    return answer


print(solution(n, lost, reserve))
