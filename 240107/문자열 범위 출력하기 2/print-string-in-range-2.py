st = input()
n = int(input())

for i in range(len(st)-2, len(st)-n-2, -1):
    print(st[i], end = "")