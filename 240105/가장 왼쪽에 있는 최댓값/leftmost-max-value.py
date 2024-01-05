n = int(input())

arr = list(map(int, input().split()))


while True:
    idx = 0
    Max = -1
    for i in range(len(arr)):
        if arr[i] > Max:
            Max = arr[i]
            idx = i
    print(idx+1, end = " ")

    if len(arr) == 1 or len(set(arr)) == 1:
        break

    arr = arr[:idx]