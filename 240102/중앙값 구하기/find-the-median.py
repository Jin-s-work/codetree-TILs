a,b,c= map(int, input().split())

if a > b:
    if b > c:
        print(b)
    elif a > c:
        print(c)
    else:
        print(a)
else:  # a < b
    if b < c:
        print(b)
    elif a > c:       # b > c
        print(a)
    else:
        print(c)