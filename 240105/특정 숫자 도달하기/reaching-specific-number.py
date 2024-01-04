arr = list(map(int, input().split()))

s = 0
cnt = 0

arr2 = []
check = False
for k in arr:
    if k >= 250:
        check = True
        break
    else:
        arr2.append(k)
    
    # s += k
    # cnt += 1



print(sum(arr2), f"{sum(arr2)/len(arr2):.1f}")


# else:
#     print(sum(arr), f"{sum(arr)/10:.1f}")