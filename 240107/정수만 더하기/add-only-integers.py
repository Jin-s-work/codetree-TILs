a = input()

ans = 0
for k in a:
    if k >= '0' and k <= '9':
        ans += int(k)
print(ans)