n = int(input())
ans = 0
for _ in range(n):
    a = int(input())
    if a % 2 != 0 and a % 3 == 0:
        ans += a

print(ans)