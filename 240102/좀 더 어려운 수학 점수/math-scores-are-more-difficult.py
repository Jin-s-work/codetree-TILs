a,b = map(int, input().split())
c,d = map(int, input().split())

if a > c:
    print("A")
elif c > a:
    print("B")
elif a == c:
    if b > d:
        print("A")
    elif d > b:
        print("B")