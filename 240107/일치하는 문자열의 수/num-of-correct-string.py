n, a = map(str, input().split())

cnt = 0
for _ in range(int(n)):
    b = input()

    if a == b:
        cnt += 1
print(cnt)