a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())


check = False

if a % 3 == 0 and b % 3 == 0 and c % 3 == 0 and d % 3 == 0 and e % 3 == 0:
    check = True

if check:
    print(1)
else:
    print(0)