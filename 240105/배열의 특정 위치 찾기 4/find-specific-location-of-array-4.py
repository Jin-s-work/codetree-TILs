arr = list(map(int, input().split()))

arr2 = []
check = False
for k in arr:
    if k == 0:
        check = True
    elif k != 0 and not check:
        if k % 2 == 0:
            arr2.append(k)

print(len(arr2), sum(arr2))