arr = []
a, b = 0, 0
for _ in range(2):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

for i in range(len(arr)):
    print(f"{sum(arr[i]) / len(arr[0]):.1f}", end = " ")
print()

ans = []
for i in range(len(arr[0])):
    s = 0
    for j in range(len(arr)):
        s += arr[j][i]
    print(f"{s / len(arr):.1f}", end = " ")
    ans.append(s)
print()

print(f"{sum(ans) // (len(arr) * len(arr[0])):.1f}")