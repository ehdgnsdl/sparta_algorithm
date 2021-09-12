# 하나의 리스트에서 모든 조합을 계산을 해야 한다면, permutations combinations 사용.
# permutations는 모든 조합의 경우를 포함. (안에 중복까지)
# combinations는 모든 조합의 경우를 포함.(안에 중복 없이)
from itertools import combinations
nums = [1, 2, 7, 6, 4]

# 소수인지 검사하는 함수.
def isPrime(a):
    if (a<2):
        return False
    for i in range(2, a):
        if (a%i==0):
            return False
    return True


# sum()은 list안에 있는 값들을 다 더해줌.
def solution(nums):
    answers = []
    answer = 0
    numbers = list(combinations(nums, 3))
    for number in numbers:
        if isPrime(sum(number)):
            answer += 1

        else:
            continue
    return answer


print(solution(nums)) # return 1