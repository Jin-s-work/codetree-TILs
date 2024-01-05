arr = list(map(int, input().split()))

for i in range(0, 8):
    k = arr[i+1] + arr[i]
    arr.append(k%10)

for k in arr:
    print(k, end = " ")