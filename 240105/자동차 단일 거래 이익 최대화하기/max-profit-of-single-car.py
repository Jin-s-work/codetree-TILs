n = int(input())

arr = list(map(int, input().split()))

arr2 = []
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        arr2.append(arr[j] - arr[i])

print(max(arr2))