s = input()
a, b = 0,0
for i in range(len(s)):
    if s[i:i+2] == 'ee':
        a += 1
    if s[i:i+2] == 'eb':
        b += 1

print(a, b)