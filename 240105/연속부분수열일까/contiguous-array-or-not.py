n1, n2 = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

check = False
for i in range(len(arr1) - len(arr2) + 1):
    if arr1[i:i+len(arr2)] == arr2:
        check = True



if check:
    print("Yes")
else:
    print("No")