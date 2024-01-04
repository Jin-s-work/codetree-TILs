n = int(input())

cnt = 1

for i in range(n):
    for j in range(n):
        print(2 * cnt % 10, end = " ")
        cnt += 1
        if cnt * 2 % 10 == 0:
            cnt += 1
    print()