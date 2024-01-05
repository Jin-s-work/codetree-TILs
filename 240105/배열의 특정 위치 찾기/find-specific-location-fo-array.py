arr = list(map(int, input().split()))

two = 0
three = 0
k = 0
for i in range(1, len(arr)+1):
    if (i-1) % 2 == 0:
        two += arr[i]
    if i % 3 == 0:
        three += arr[i-1]
        k += 1
print(two, f"{three/k:.1f}")

## 2 5 8