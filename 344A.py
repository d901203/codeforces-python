n = int(input())
a = []
for _ in range(n):
    a.append(input())
result = 1
for i in range(1, n):
    if a[i - 1][-1] == a[i][0]:
        result += 1
print(result)
