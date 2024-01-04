a, b = map(int, input().split())

for i in range(1,5):
    for j in range(b, a-1, -1):
        if j == a:
            print(f"{j} * {2*i} = {2*j*i}", end = " ")
        else:
            print(f"{j} * {2*i} = {2*j*i}", end = " / ")
    print()