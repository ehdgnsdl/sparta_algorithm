numbers = [1, 2, 3, 4, 6, 7, 8, 0]  # 9, 5를 더해서 14. # 길이 8

# num의 총 합에서 numbers의 총 합을 빼준 값을 반환할 것임.
def solution(numbers):
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] # 길이: 10
    sum = 0 # numbers의 총 합
    answer = 0 # num의 총 합.
    for i in range(len(num)):
        answer += num[i]
    for i in range(len(numbers)):
        sum += numbers[i]

    answer -= sum

    return answer


print(solution(numbers))
