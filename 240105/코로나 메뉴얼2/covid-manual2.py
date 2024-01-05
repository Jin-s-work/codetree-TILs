a, b = map(str, input().split())
d, c = map(str, input().split())
f, e = map(str, input().split())

x,y,z,w = 0,0,0,0
cnt = 0
if int(b) >= 37 and a == 'Y':
    x += 1
elif int(b) >= 37 and a == 'N':
    y += 1
elif int(b) < 37 and a == 'Y':
    z += 1
else:
    w += 1

if int(c) >= 37 and d == 'Y':
    x += 1
elif int(c) >= 37 and d == 'N':
    y += 1
elif int(c) < 37 and d == 'Y':
    z += 1
else:
    w += 1

if int(e) >= 37 and f == 'Y':
    x += 1
elif int(e) >= 37 and f == 'N':
    y += 1
elif int(e) < 37 and f == 'Y':
    z += 1
else:
    w += 1

print(x, y, z, w, end = " ")

if x >= 2:
    print("E")