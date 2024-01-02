# a = 5
# b = 6
# c = 7
a, b, c = 5, 6, 7
tmpb = b
tmpc = c
b = a
c = tmpb
a = tmpc

print(a)
print(b)
print(c)