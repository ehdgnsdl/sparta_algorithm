# 코딩테스트 연습 / 제목: 예산
# https://programmers.co.kr/learn/courses/30/lessons/12982

d = [1, 3, 2, 5, 4]
budget = 9

def solution(d, budget):
    d.sort() # d 배열을 오름차순으로 정렬
    while budget < sum(d): # budget < sum(d)를 만족할 때까지, while문을 돌면서 d.pop()을 진행
        d.pop() # d.pop()은 뒤에서부터 하나씩 뺀다.
    return len(d) # while문이 끝나고나서의 d 배열의 길이를 반환

print(solution(d, budget))