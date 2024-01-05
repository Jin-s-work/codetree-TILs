arr = list(map(int, input().split()))
arr2 = [0] * 11
for k in arr:
    if k == 0:
        break
    else:
        arr2[k // 10] += 1

for i in range(10, 0, -1):
    print(f"{i * 10} - {arr2[i]}")