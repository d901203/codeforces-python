n = int(input())
a = list(map(int, input().split()))
result = [0] * n
for i, x in enumerate(a):
    result[x - 1] = i + 1
print(*result)
