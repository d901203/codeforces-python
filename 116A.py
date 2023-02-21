n = int(input())
c = result = 0
for _ in range(n):
    a, b = map(int, input().split())
    c -= a
    c += b
    result = max(result, c)
print(result)
