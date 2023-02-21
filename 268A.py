n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
result = 0
for i in range(n):
    for j in range(n):
        if a[i][0] == a[j][1]:
            result += 1
print(result)
