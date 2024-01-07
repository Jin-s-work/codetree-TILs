a = input()

for k in a:
    if (k <= 'z' and k >= 'a') or (k <= 'Z' and k >= 'A'):
        print(k.lower(), end = "")
    elif (k >= '0' and k <= '9'):
        print(k, end = "")