input = [3, 5, 6, 1, 2, 4]


def find_max_num(array):
    # 리스트의 첫 번째 원소를 max_values에 저장
    max_values = array[0]

    #for문이 돌아감.
    for num in array:
        if max_values < num:
            max_values = num
    return max_values


result = find_max_num(input)
print(result)