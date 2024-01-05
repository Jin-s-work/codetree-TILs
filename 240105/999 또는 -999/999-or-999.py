arr = list(map(int, input().split()))

Max = -1
Min = 1000
for k in arr:
    if k == 999 or k == -999:
        break
    else:
        if k < Min:
            Min = k
        if k > Max:
            Max = k

print(Max, Min)