s = input()

arr = list(s)
arr.pop(1)
arr.pop(len(arr)-2)

s = ''.join(arr)

# s = s[:2] + s[3:-2] + s[-1:]

print(s)