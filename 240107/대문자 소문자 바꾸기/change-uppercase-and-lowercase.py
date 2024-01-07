a = input()

for k in a:
    if k >= 'a' and k <= 'z':
        print(k.upper(), end = "")
    elif k >= 'A' and k <= 'Z':
        print(k.lower(), end = "")