n = int(input())

arr = list(map(float, input().split()))


av = sum(arr) / len(arr)

print(f"{av:.1f}")
if av >= 4.0:
    print("Perfect")
elif av >= 3.0:
    print("Good")
else:
    print("Poor")