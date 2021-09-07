input = [4, 6, 2, 9, 1]

#1. [4 6 2 9 1]
#    - - - - -
#2. [1 6 2 9 4]
#      - - - -
#3. [1 2 6 9 4]
#        - - -
#4. [1 2 4 9 6]
#          - -

#for i in range(5-1):
#    for j in range(5-i):
#        print(i+j)

def selection_sort(array):
    n = len(array)

    for i in range(n - 1):
        min_index = i
        for j in range(n - i):
            if array[i + j] < array[min_index]:
                min_index = i+j
            array[i], array[min_index] = array[min_index], array[i]
    return


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!