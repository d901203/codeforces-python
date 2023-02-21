n = int(input())
result = 0
for _ in range(n):
    ans = sum(map(int, input().split()))
    if ans >= 2:
        result += 1
print(result)
 