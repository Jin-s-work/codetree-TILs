arr = list(map(int, input().split()))

Max = -1

for k in arr:
    if Max < k:
        Max = k
print(Max)