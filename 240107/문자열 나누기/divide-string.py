n = int(input())

arr = list(map(str, input().split()))

ans = ""

for k in arr:
    ans += k

for i in range(0, len(ans), 5):
    for j in range(5):
        if i+j < len(ans):
            print(ans[i+j], end = "")
    print()