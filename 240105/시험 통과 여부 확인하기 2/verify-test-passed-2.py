n = int(input())
cnt = 0
for i in range(n):
    score = []
    score = list(map(int, input().split()))
    if (sum(score) // len(score)) >= 60:
        print("pass")
        cnt += 1
    else:
        print("fail")

print(cnt)