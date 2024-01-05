n1, n2 = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

cnt = 0
for i in range(len(arr2)-1):
    if arr1.index(arr2[i]) + 1 == arr1.index(arr2[i+1]):
        cnt += 1


if cnt + 1 == len(arr2):
    print("Yes")
else:
    print("No")