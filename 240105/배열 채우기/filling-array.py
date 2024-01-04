arr = []

arr = list(map(int, input().split()))
arr2 = []
check = False
for k in arr:
    if k != 0 and not check:
        arr2.append(k)
    else:
        check = True
    
for i in range(len(arr2)):
    print(arr2[len(arr2)-i-1], end = " ")