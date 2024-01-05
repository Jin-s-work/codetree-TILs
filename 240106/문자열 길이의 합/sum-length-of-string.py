n = int(input())
s = 0
cnt = 0
for _ in range(n):
    a = input()
    s += len(a)
    if a[0] == 'a':
        cnt += 1
print(s, cnt)