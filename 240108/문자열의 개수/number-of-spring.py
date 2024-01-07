cnt = 0
idx = 0
arr = []
while True:
    n = input()
    idx += 1
    if n == '0':
        print(cnt)
        for k in arr:
            print(k)
        break
    
    if idx % 2 != 0:
        arr.append(n)
    cnt += 1