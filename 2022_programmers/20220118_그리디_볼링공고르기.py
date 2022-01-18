from itertools import *
a = list(map(int, input().split()))
b = list(map(int, input().split()))

count = 0
c = list(combinations(b, 2))

for i in range(len(c)):
    if c[i][0] != c[i][1]:
        count += 1

print(count)
