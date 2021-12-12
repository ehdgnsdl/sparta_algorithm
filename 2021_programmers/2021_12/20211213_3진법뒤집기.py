# 코딩테스트 연습 / 제목: 내적
# https://programmers.co.kr/learn/courses/30/lessons/68935

n = 45;

def solution(n):
    result = '' # 나머지들을 저장할 result (45%3 = 0, 15%3 = 0, 5%3 = 2, 1%3=1)
    # 역순으로하면 자연수 45의 3진법은 1200이다. 이를 뒤집으면 0021
    while n:
        result+=str(n%3) # 처음 45 / 3 ... 나머지 0
        n = n//3 # 몫이 15가 됨.(n = 45 -> n = 15)
        print(result)
    return int(result,3)

print(solution(n))
