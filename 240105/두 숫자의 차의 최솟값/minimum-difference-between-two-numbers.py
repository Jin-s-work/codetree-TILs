n = int(input())

arr = list(map(int, input().split()))

Min = 101
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[j] - arr[i] < Min:
            Min = arr[j] - arr[i]
            
print(Min)