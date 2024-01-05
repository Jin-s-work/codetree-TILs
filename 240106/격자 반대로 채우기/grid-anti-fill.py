n = int(input())

arr = [[0] * n for _ in range(n)]

cnt = 1
check = False
if n % 2 == 0:
    check = True
for i in range(n-1, -1, -1):
    if (i % 2 == 0 and not check) or (i % 2 != 0 and check):
        for j in range(n-1, -1, -1):
            arr[j][i] = cnt
            cnt += 1
    else:
        for j in range(n):
            arr[j][i] = cnt
            cnt += 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end = " ")
    print()