data = input()

count0 = 0 # 전부 0으로 바꾸는 경우
count1 = 0 # 전부 1로 바꾸는 경우

# 첫 번째 원소에 대해서 처리
if data[0] == '1':
    # 모두 0으로 바뀌는 것
    count0 += 1
else:
    # 모두 1로 바뀌는 것
    count1 += 1
    

for i in range(len(data)-1):
    if data[i] != data[i+1]:
        # 다음 수에서 1로 바뀌는 경우
        if data[i+1] == '1':
            count0 += 1
        # 다음 수에서 0으로 바뀌는 경우
        else:
            count1 += 1


print(min(count0, count1))



