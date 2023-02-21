n = int(input())
a = list(map(int, input().split()))
result = 0
mn = mx = a[0]
for x in a[1:]:
    if x > mx:
        result += 1
        mx = x
    elif x < mn:
        result += 1
        mn = x
print(result)
