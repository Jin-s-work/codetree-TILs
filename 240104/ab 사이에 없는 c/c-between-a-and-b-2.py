a, b, c = map(int, input().split())

check = False
for i in range(a, b+1):
    if i % c == 0:
        check = True

if check:
    print("NO")
else:
    print("YES")