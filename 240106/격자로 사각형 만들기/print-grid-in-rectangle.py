n = int(input())

arr = [[1] * n for _ in range(n)]

for i in range(n-1):
    for j in range(n-1):
        arr[i+1][j+1] = arr[i][j] + arr[i+1][j] + arr[i][j+1]


for i in range(n):
    for j in range(n):
        print(arr[i][j], end = " ")
    print()