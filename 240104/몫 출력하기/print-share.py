cnt = 0
try:
    while True:
        if cnt == 4:
            break
        a = int(input())
    
        if a % 2 == 0:
            print(a // 2)
            cnt += 1
except EOFError:
    pass