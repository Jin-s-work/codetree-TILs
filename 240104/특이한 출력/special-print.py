n = int(input())

for i in range(1,1+n):
    for j in range(1,1+n):
        print(f"({i}, {j})", end = " ")
        if (i+j) % 4 == 0:
            print()