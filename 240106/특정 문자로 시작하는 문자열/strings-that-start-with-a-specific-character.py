n = int(input())

arr = []
for _ in range(n):
    a = input()
    arr.append(a)

m = input()

cnt = 0
s = 0
for k in arr:
    if k[0] == m:
        cnt += 1
        s += len(k)

print(cnt, f"{s/cnt:.2f}")