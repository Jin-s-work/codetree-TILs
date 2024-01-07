st = input()
n = int(input())

if n > len(st):
    print(st)
else:
    print(st[-n:][::-1])

    # for i in range(len(st)-1, len(st)-n-1, -1):
    #     print(st[i], end = "")