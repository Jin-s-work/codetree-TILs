n = int(input())

arr = []
arr.append(1)
arr.append(n)

k = 0
i = 0

print(1, n, end = " ")
while True:
    k = arr[i] + arr[i+1]
    print(k, end = " ")
    if k > 100:
        break
    arr.append(k)
    i += 1