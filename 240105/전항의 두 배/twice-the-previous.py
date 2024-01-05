arr = list(map(int, input().split()))

for i in range(8):
    k = arr[i+1] + 2 * arr[i]
    arr.append(k)


for k in arr:
    print(k, end = " ")