arr = list(map(int, input().split()))

arr2 = []
for k in arr:
    if k == 0:
        break
    else:
        arr2.append(k//10)



for i in range(1, 10):
    print(f"{i} - {arr2.count(i)}")