n = int(input())

arr = list(map(int, input().split()))

arr2 = []
Max = -1
for i in range(len(arr)):
    if arr[i] > Max:
        Max = arr[i]
        idx = i
        arr2.append(idx+1)

for i in range(len(arr2)-1, -1, -1):
    print(arr2[i], end = " ")