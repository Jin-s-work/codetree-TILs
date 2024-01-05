n, q = map(int, input().split())

arr = list(map(int, input().split()))

for _ in range(q):
    quest = list(map(str, input().split()))
    if int(quest[0]) == 1:
        print(arr[int(quest[1])-1])
    elif int(quest[0]) == 2:
        if int(quest[1]) in arr:
            print(arr.index(int(quest[1]))+1)
        else:
            print(0)
    else:
        for i in range(int(quest[1]), int(quest[2])+1):
            print(arr[i-1], end = " ")