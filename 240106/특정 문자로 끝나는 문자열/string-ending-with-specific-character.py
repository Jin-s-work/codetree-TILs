arr = []
for i in range(10):
    a = input()
    arr.append(a)

m = input()

check = False
for k in arr:
    if k[len(k) - 1] == m:
        print(k)
        check = True

if not check:
    print("None")