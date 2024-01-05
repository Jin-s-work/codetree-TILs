arr = list(map(int, input().split()))

a = -1
b = 1001
for k in arr:
    if k > 500 and b > k:
        b = k
    elif k < 500 and a < k:
        a = k
        
print(a, b)