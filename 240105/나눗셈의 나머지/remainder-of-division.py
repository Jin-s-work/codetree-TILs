a, b = map(int, input().split())
arr = [0] * 10
s = 0
while a > 1:
    arr[((a % b) * (a % b))] += 1
    a = a // b
    

for k in arr:
    s += k*k
    
print(s)