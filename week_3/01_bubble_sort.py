input = [4, 6, 2, 9, 1]

#  -> -> -> ->
# [4, 6, 2, 9, 1]
# -> -> ->
# [4, 2, 6, 1, 9]
# -> ->
# [2, 4, 1, 6, 9]
# ->
# [2, 1, 4, 6, 9]

#for i in range(5 - 1)
#    for j in range(5 - 1 -i):
#        if array[j] > array[j+1]:
#            교환

def bubble_sort(array):
    n = len(array) # array의 길이를 n에 저장 / # O(N^2)
    for i in range(n-1): # ex) 5-1 = 4번 반복 / n의 길이
        for j in range(n-1-i): # 5-i-1번 반복 / n의 길이
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


bubble_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!