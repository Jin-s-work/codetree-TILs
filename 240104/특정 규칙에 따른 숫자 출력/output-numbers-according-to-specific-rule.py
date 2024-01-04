n = int(input())

cnt = 1
for i in range(n):
    for j in range(i):
        print(" ", end = " ")
    for j in range(n-i):
        print(cnt % 10, end = " ")
        cnt += 1
        if cnt % 10 == 0:
            cnt += 1
    print()