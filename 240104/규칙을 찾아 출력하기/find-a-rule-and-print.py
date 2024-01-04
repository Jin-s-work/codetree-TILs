n = int(input())

for i in range(n):
    for j in range(n):
        if i != 0 and j != 0 and i != n-1 and j != n-1 and i <= j:
            print(" ", end = " ")
        elif i == n-1 or j == n-1:
            print("*", end = " ")
        else:
            print("*", end = " ")
        # elif i != 0 and j != 0 and i >= j:
    print()