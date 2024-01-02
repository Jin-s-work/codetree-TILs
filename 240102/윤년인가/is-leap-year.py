a = int(input())

if (a % 4 == 0):
    if a % 100 == 0 and a % 400 != 0:
        print("false")
    elif a % 100 == 0 and a % 400 == 0:
        print("true")
    else:
        print("true")
else:
    print("false")