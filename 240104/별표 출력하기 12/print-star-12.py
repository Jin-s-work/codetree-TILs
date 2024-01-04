n = int(input())

for i in range(n):
    for j in range(n):
        if j % 2 == 0 and i == 0:
            print("*", end = " ")
        elif j % 2 == 0 and i != 0:
            print(" ", end = " ")
        elif j % 2 != 0 and i <= j:
            print("*", end = " ")
        elif j % 2 != 0 and i > j:
            print(" ", end = " ")
    print()