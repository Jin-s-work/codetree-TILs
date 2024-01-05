n, m = map(int, input().split())

arr = [[0] * m for _ in range(n)]

cnt = 1
for i in range(n+m-1):
    for j in range(max(0, i-m+1), min(i, n-1) + 1):
        arr[j][i-j] = cnt
        cnt += 1

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = " ")
    print()