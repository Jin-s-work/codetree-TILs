a, b = map(int, input().split())

c = b * 100 * 100 // (a * a)

print(c)
if c >= 25:
    print("Obesity")