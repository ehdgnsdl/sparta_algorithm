seat_count = 9
vip_seat_array = [4, 7]

# [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# 좌석 [1, 2] 2
# [1, 2] [2, 1]
#
# 좌석 [1, 2, 3] 3
# [1, 2, 3] [2, 1, 3], [1, 3, 2]
#
# 좌석 [1, 2, 3, 4] 5
# [1, 2, 3, 4] [1, 2, 4, 3] [1, 3, 2, 4] [2, 1, 3, 4]
# [2, 1, 4, 3]
#
# 좌석 [1,2, 3, 4, 5] 8

# 피보나치 수열
# 좌석(2) = 2
# 좌석(3) = 3

memo = {
    1: 1,
    2: 2
}


# [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# 1, 2, 3, F(3) = 3
#
# 5, 6 F(2) = 2
#
# 8, 9 F(2) = 2
#  3 * 2 * 2 = 12

def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]
    nth_fibo = fibo_dynamic_programming(n - 1, fibo_memo) + fibo_dynamic_programming(n - 2, fibo_memo)
    fibo_memo[n] = nth_fibo

    return nth_fibo


def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    all_ways = 1
    current_index = 0
    # [4, 7]
    for fixed_seat in fixed_seat_array:
        fixed_seat_index = fixed_seat - 1  # index는 fixed_seat값의 -1한 값

        # fixed_seat_index-current_index는 개수를 말함
        count_of_ways = fibo_dynamic_programming(fixed_seat_index - current_index, memo)
        all_ways *= count_of_ways  # 곱 연산
        current_index = fixed_seat_index + 1  # 다음 칸으로 넘겨준다.

    # for문이 끝나면 current_index가 7까지 갔을 것이다.
    count_of_ways = fibo_dynamic_programming(total_count - current_index, memo)
    all_ways *= count_of_ways  # 곱 연산

    return all_ways


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))
