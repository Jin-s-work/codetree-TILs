a = input()
b = input()

while b in a:
    for i in range(len(a)):
        if a[i:i+len(b)] == b:
            a = a[:i] + a[i+len(b):]

print(a)