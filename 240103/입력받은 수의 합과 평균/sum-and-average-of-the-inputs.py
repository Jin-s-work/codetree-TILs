n = int(input())

s = 0
k = 0
for _ in range(n):
    a = int(input())
    s += a
    k += 1

print(s, f"{s/k:.1f}")