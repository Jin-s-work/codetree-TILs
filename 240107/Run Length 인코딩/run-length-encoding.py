st = input()
arr = []

for k in st:
    arr.append(k)


ans = ""
tmp = ""
cnt = 1
for i in range(len(arr)):
    if i == 0:
        tmp = arr[0]
    else:
        if tmp == arr[i]:
            cnt += 1
        else:
            ans += tmp
            ans += str(cnt)
            tmp = arr[i]
            cnt = 1

ans += tmp
ans += str(cnt)
tmp = arr[i]
cnt = 1

print(len(ans))
print(ans)