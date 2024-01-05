arr = []
for i in range(4):
    tmp = list(map(int, input().split()))
    arr.append(tmp)

ans = []
for i in range(4):
    for j in range(4):
        if i >= j:
            ans.append(arr[i][j])

print(sum(ans))