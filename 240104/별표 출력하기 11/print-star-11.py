n = int(input())

for i in range(2*n+1):
    for j in range(2*n+1):
        if i % 2 != 0 and j % 2 != 0:
            print(" ", end = " ")
            continue
        print("*", end = " ")
    print()