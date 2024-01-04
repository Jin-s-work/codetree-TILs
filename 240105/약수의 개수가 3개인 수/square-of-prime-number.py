import math
a, b = map(int, input().split())

cnt = 0
for i in range(a, b+1):
    if int(math.sqrt(i)) == math.sqrt(i) and i != 1:
        cnt += 1
print(cnt)