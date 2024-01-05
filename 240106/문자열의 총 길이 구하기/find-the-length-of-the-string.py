arr = list(map(str, input().split()))

s = 0
for i in range(len(arr)):
    s += len(arr[i])

print(s)