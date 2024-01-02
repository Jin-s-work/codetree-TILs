a,b = map(str, input().split())
c,d = map(str, input().split())
e,f = map(str, input().split())

cnt = 0

if a == 'Y' and int(b) >= 37:
    cnt += 1
if c == 'Y' and int(d) >= 37:
    cnt += 1
if e == 'Y' and int(f) >= 37:
    cnt += 1

if cnt >= 2:
    print("E")
else:
    print("N")