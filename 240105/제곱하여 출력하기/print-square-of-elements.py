n = int(input())

arr = list(map(int, input().split()))

arr = [k * k for k in arr]

for k in arr:
    print(k, end = " ")