st = input()

ans = ""
for i in range(1, len(st), 2):
    ans += st[i]

print(ans[::-1])