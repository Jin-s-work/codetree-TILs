a = input()

for k in a:
    if (k >= 'A' and k <= 'Z') or (k >= 'a' and k <= 'z'):
        print(k.upper(), end = "")