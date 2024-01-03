n  = int(input())

i = 0
while True:
    if n == 2 ** i:
        print(i)
        break
    i += 1