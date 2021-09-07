# BOJ 1158
def josephus_problem(n, k):
    result_arr = []
    next_index = k-1
    arr = list(range(1, n+1))
    while arr:
        num = arr.pop(next_index)
        result_arr.append(num)
        if len(arr) != 0:
            next_index = (next_index + (k-1)) % len(arr)
    print("<", ", ".join(map(str, result_arr)), ">", sep ='')


n, k = map(int, input().split())
josephus_problem(n, k)
