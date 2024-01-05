arr = list(map(int, input().split()))

arr2 = []
for k in arr:
    if k == 0:
        break
    else:
        arr2.append(k)

print(sum(arr2[-3:]))