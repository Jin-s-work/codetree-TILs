import math
n = int(input())

check = False
for i in range(2, int(math.sqrt(n) + 1)):
    if n % i == 0:
        check = True

if check:
    print("C")
else:
    print("N")