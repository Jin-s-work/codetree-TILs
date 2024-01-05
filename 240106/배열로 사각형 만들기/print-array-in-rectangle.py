arr = [[0] * 5 for _ in range(5)]
for i in range(5):
    arr[i][0] = 1
    arr[0][i] = 1

for i in range(4):
    for j in range(4):
        arr[i+1][j+1] = arr[i][j+1] + arr[i+1][j]

for i in range(5):
    for j in range(5):
        print(arr[i][j], end = " ")
    print()