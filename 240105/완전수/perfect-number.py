a, b = map(int, input().split())

cnt = 0
for i in range(a, b+1):
    s = 0
    for j in range(1,i):
        if i % j == 0:
            s += j
    if s == i:
        cnt += 1
    
print(cnt)