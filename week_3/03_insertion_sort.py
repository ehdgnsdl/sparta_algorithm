input = [4, 6, 2, 9, 1]


# 1. [4 6 2 9 1]
#     <-
# 2. [4 6 2 9 1]
#     <-<-
# 3. [2 4 6 9 1]
#     <-<-<- / 이미 크므로 break
# 4. [2 4 6 9 1]
#     <-<-<-<-

# for i in range(1, 5):
#    for j in range(i):
#        print(i-j)

# bubble_sort, selection_sort : O(N^2)
# [1 2 3 4 5]


def insertion_sort(array): # 시간복잡도 최악 O(N^2) , 최선은 O(N)
    n = len(array)
    for i in range(1, n):
        for j in range(i):
            if array[i - j - 1] > array[i - j]: # i-j-1은 i-j번째의 앞에 것. 즉, 둘이 비교해서 앞에 있는 것이 크다면 교환
                array[i-j-1], array[i - j] = array[i-j], array[i-j-1]
            else:
                break
    return


insertion_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
