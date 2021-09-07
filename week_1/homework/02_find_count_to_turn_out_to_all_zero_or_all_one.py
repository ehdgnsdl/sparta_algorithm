input = "011110"
# 011110
# 모두 0으로 만드는 방법에서 최소로 뒤집는 숫자
# count_to_all_zero
# 0->1로 문자열이 전한되는 순간 count_to_all_zero+=1

# 모두 1으로 만드는 방법에서 최소로 뒤집는 숫자
# count_to_all_one
# 1->0로 문자열이 전한되는 순간 count_to_all_one+=1

# 1) 뒤집어질 때, 즉 0에서 1 혹은 1에서 0으로
# 2) 첫 번째 원소가 0인지 1인지에 따라서 숫자를 추가해줘야함.

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_all_zero = 0
    count_to_all_one = 0
    if string[0] == '0':
        count_to_all_one += 1
    elif string[0] == '1':
        count_to_all_zero += 1

    for i in range(len(string)-1):
        if string[i] != string[i+1]: #1 -> 0 0 -> 1
            if string[i+1] == '0':
                count_to_all_one += 1
            if string[i+1] == '1':
                count_to_all_zero += 1
    return min(count_to_all_one, count_to_all_zero)



result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)