s = input()

a = s[0]
b = s[1]

ans = ""
for k in s:
    if k == a:
        ans += b
    elif k == b:
        ans += a
    else:
        ans += k

print(ans)