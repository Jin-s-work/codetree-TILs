s = input()

arr = input()

for k in arr:
    if k == 'L':
        s = s[1:] + s[0]
    elif k == 'R':
        s = s[-1] + s[:-1]


print(s)