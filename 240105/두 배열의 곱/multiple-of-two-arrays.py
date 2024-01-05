# arr1 = [[0] * 3 for _ in range(3)]
# arr2 = [[0] * 3 for _ in range(3)]
arr1 = []
arr2 = []

for i in range(3):
    arr = list(map(int, input().split()))
    arr1.append(arr)

blank = list(map(int, input().split()))
for i in range(3):
    arr = list(map(int, input().split()))
    arr2.append(arr)


for i in range(3):
    for j in range(3): 
        print(arr1[i][j] * arr2[i][j], end = " ")
    print()