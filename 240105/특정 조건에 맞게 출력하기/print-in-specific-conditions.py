arr = list(map(int, input().split()))

arr2 = []

for k in arr:
    if k == 0:
        break
    else:
        arr2.append(k)

for k in arr2:
    if k % 2 != 0:
        print(k + 3, end = " ")
    else:
        print(k//2, end = " ")