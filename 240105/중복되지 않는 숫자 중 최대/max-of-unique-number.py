n = int(input())

arr = list(map(int, input().split()))

Max = -1
cnt = 0
for i in range(len(arr)):
    if arr[i] > Max and arr.count(arr[i]) == 1:
        Max = arr[i]

print(Max)