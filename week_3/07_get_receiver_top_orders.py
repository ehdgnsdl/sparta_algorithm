top_heights = [6, 9, 5, 7, 4]

# [0, 0, 2, 2, 4]
# [0, 0, 0, 0, 0]

#  <- <- <- <- <-
#  6  9  5  7  4
#  [0, 0, 0, 0, 4]

# <- <- <- <-
# 6  9  5   7
# [0, 0, 0, 2, 4]

# <- <- <-
# 6  9  5
# [0, 0, 2, 2, 4]

# <- <-
# 6 9
# [0, 0, 2, 2, 4]

# <-
# 6
# [0, 0, 2, 2, 4]

#for idx in range((5-1), 0, -1): # 시작하는점, 끝나는 점, 어떻게 연산을 줄여갈 것인가
#    print(idx)

#[ 6, 9, 5, 7, 4]
#[ 0, 0, 0, 0, 4]
def get_receiver_top_orders(heights):
    answer = [0] * len(heights)
    while heights: #heights가 빈상태가 아닐 때까지
        height = heights.pop()
        # [ 6, 9, 5, 7]
        for idx in range(len(heights)-1, 0, -1):
            if heights[idx] > height:
                answer[len(heights)] = idx + 1
                break
    return answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!