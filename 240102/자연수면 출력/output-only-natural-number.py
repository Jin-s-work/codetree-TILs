a, b = map(float, input().split())

if a == int(a) and a > 0:
    for _ in range(int(b)):
        print(int(a), end = "")
if a <= 0:
    print("0")