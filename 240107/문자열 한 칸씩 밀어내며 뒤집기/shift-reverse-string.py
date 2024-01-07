s, q = map(str, input().split())

for i in range(int(q)):
    a = int(input())

    if a == 1:
        s = s[1:] + s[0]
        print(s)
    elif a == 2:
        s = s[-1] + s[:-1]
        print(s)
    elif a == 3:
        s = s[::-1]
        print(s)