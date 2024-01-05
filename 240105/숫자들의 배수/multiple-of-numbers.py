n = int(input())

arr = [k * n for k in range(1, 12)]

cnt = 0
for k in arr:
    print(k, end = " ")
    if k % 5 == 0:
        cnt += 1
    if cnt == 2:
        break