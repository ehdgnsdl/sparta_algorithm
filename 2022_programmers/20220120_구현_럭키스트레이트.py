a = input()

b = int(len(a) / 2)
result1 = 0
result2 = 0

for i in range(b):
    result1 += int(a[i])

for j in range(b, len(a)):
    result2 += int(a[j])

if result1 == result2:
    print("LUCKY")
else:
    print("READY")