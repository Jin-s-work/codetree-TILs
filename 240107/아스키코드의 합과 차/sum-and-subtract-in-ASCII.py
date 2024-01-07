a, b = map(str, input().split())

x = ord(a)
y = ord(b)

if x >= y:
    print(x+y, x-y)
else:
    print(x+y, y-x)