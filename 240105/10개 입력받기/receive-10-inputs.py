arr = list(map(int, input().split()))

check = False
arr2 = []
for k in arr:
    if k == 0:
        check = True
    elif k != 0 and not check:
        arr2.append(k)

print(sum(arr2), f"{sum(arr2) / len(arr2):.1f}")