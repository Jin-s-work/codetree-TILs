a, b = map(str, input().split())

if b in a:
    print(a.find(b))
else:
    print("No")