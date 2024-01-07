n = int(input())


ans = 0

for _ in range(n):
    st = int(input())
    ans += st

ans = str(ans)

ans = ans[1:] + ans[0]

print(ans)