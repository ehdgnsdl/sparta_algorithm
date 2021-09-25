left = 13
right = 17

# 약수 개수 구하는 함수
def measure(input_num):
    count = 0 # 약수의 개수
    for a in range(1, input_num + 1):
        if input_num == a:
            print(a)
            count += 1
        elif input_num % a == 0:
            print(a, end=', ')
            count += 1
    return count


def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        if measure(num) % 2 == 0: # 짝수라면
            answer += num
        else:
            answer -= num
    return answer

print(solution(left, right))