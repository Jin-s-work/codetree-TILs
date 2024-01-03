s = 0
k = 0
while True:
    a = int(input())
    if a < 20 or a >= 30:
        break
    s += a
    k += 1
print(f"{s/k:.2f}")