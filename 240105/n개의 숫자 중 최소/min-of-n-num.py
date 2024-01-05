import sys
n = int(input())

arr = list(map(int, input().split()))

cnt = 0
Min = sys.maxsize
for k in arr:
    if k <= Min:
        Min = k

for k in arr:
    if k == Min:
        cnt += 1
    
print(Min, cnt)