s = 0
k = 0
for _ in range(10):
    a = int(input())
    if 0<=a<=200:
        s += a
        k += 1

print(s, f"{s/k:.1f}")