n = int(input())

for i in range(n):
    for j in range(2*i):
        print(" ", end = "")
    for j in range(2*n -2 * i - 1):
        print("*", end = " ")
    
    print()
for i in range(2, n+1):
    for j in range(2*n - 2*i):
        print(" ", end = "")
    for j in range(2 * i - 1):
        print("*", end = " ")
    
    print()