n, m = map(int, input().split())

arr = [[0] * m for _ in range(n)]
num = 1
for i in range(n):
    for j in range(m):
        arr[i][j] = num
        num += 1

for k in arr:
    for l in k:
        print(l, end = " ")
    print()