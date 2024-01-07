a = input()
b = input()

cnt = 0
for i in range(len(a)):
    if a[i:i+len(b)] == b:
        cnt += 1

print(cnt)