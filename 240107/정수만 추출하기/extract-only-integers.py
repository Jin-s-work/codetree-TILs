a, b = map(str, input().split())

aa = ""
bb = ""
for k in a:
    if not (k >= '0' and k <= '9'):
        break
    else:
        aa += k
for k in b:
    if not (k >= '0' and k <= '9'):
        break
    else:
        bb += k

print(int(aa) + int(bb))