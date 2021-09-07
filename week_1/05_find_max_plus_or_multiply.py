input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    sum = 0
    for num in array:
        if num <= 1 or sum <= 1:
            sum += num
        else:
            sum *= num
    return sum


result = find_max_plus_or_multiply(input)
print(result)
