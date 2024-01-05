n, m = map(int, input().split())

arr = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

arr2 = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    arr2.append(tmp)

for i in range(n):
    for j in range(m):
        if arr[i][j] != arr2[i][j]:
            print(1, end = " ")
        else:
            print(0, end = " ")
    print()