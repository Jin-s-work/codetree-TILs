cnt = 0

n = int(input())

while True:
    if n % 2 == 0:
        n = n * 3 + 1
    else:
        n = 2 * n + 2
    cnt += 1
    if n >= 1000:
        print(cnt)
        break