# N은 모험가의 수
N = int(input())
# 공포도가 적힌 멤버
X = list(map(int, input().split()))
X.sort() # 1 2 2 2 3
count = 0 # 포함되는 그룹
result = 0 # 총 그룹 수

for i in X: # 오름차순된 그룹을 하나씩 꺼내서 확인.
    count += 1 # 한 멤버를 추가시킨다.
    if count >= i: # count가 i보다 크거나 같으면
        result += 1 # 총 그룹수 추가
        count = 0 # 멤버 수 초기화

print(result)
