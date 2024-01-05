n = int(input())
arr = list(map(int, input().split()))

arr2 = [k for k in arr if k % 2 == 0]

for k in arr2:
    print(k, end = " ")