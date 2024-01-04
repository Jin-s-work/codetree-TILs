import math
n = int(input())

check = False
for i in range(1, int(math.sqrt(n))):
    if n % i == 0:
        check = True

if check:
    print("C")
else:
    print("N")