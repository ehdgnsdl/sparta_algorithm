# 리스트에서 두 개의 원소로 할 수 있는 조합을 구하려면 itertools를 이용
# from itertools import product
# from itertools import permutations
from itertools import combinations
# 하나의 리스트에서 구할 때는 permutations과 combinations를 사용하면 되고 두 개 이상의 리스트에서 구할 때는 product를 사용하면 됩니다. permutations은 정확히는 순열이 되고 combinations는 조합
# permutations는 순열이기에 결과값에 순서가 영향이 있을 때 사용하시면 됩니다.
# combinations는 조합이기에 순서가 영향력이 없을 때 사용하시면 됩니다.

numbers = [2, 1, 3, 4, 1]

def solution(numbers):
    a = []
    b = []
    a = list(combinations(numbers, 2))
    
    for i in range(len(a)):
        answer = 0
        for j in range(2):
            answer += a[i][j] # a[i][j]는 각 튜플에 있는 두 수를 더한 후에 answer에 저장
        b.append(answer) # 두 수를 더한 answer 값을 append()를 이용해서 배열 안에 저장
    b = list(set(b)) # set() 함수를 이용해서 집합으로 만들어서 중복 제거
    b.sort() # 오름차순으로 정렬
        
    return b

print(solution(numbers))