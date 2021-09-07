from collections import deque


def solution(prices):
    result_arr = []
    prices = deque(prices)


    while prices:
        non_drop_count = 0
        current_price = prices.popleft()

        for next_price in prices:
            print(next_price)
            if current_price > next_price:
                non_drop_count += 1
                break
            non_drop_count += 1
        result_arr.append(non_drop_count)
    return result_arr


prices = list(map(int, input().split()))
print(solution(prices))
