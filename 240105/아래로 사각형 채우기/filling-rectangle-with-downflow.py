n = int(input())

arr = [[0] * n for _ in range(n)]

cnt = 1
for i in range(n):
    for j in range(n):
        arr[j][i] = cnt
        cnt += 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end = " ")
    print()