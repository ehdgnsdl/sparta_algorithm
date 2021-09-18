price = 3
money = 20
count = 4

# 3 + 6 + 9 + 12

def solution(price, money, count):


    sum = 0
    # range 1부터 4까지 반복
    for i in range(1, count+1):
        sum += price * i
    # 금액이 부족하지 않으면 0을 return
    if sum-money < 0:
        return 0
    return sum-money


print(solution(price, money, count))