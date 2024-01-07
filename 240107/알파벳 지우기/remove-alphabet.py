a = input()
b = input()

aa = ""
bb = ""
for k in a:
    if not (k >= '0' and k <= '9'):
        continue
    else:
        aa += k
for k in b:
    if not (k >= '0' and k <= '9'):
        continue
    else:
        bb += k


print(int(aa) + int(bb))