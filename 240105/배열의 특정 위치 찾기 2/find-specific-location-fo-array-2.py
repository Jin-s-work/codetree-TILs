arr = list(map(int, input().split()))

s = 0
t = 0
for i in range(10):
    if i % 2 == 0:
        s += arr[i]
    else:
        t += arr[i]

if s >= t:
    print(s - t)
else:
    print(t - s)