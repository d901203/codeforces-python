n = int(input())
a = list(map(int, input().split()))
result = [0, 0]
i = 0
j = n - 1
k = 0
while i <= j:
    if a[i] > a[j]:
        result[k] += a[i]
        i += 1
    else:
        result[k] += a[j]
        j -= 1
    k ^= 1
print(*result)
