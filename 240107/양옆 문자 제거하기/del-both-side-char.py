s = input()

arr = list(s)
arr.pop(2)
arr.pop(len(arr)-2)

s = ''.join(arr)
print(s)