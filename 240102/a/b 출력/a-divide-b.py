a, b = map(int, input().split())

print(f"{a//b}.", end = "")

a %= b

for _ in range(20):
    a *= 10
    # 10으로 곱한 다음 나누어야 나머지를 제대로 알 수 있다.
    print(a//b, end = "")
    a %= b