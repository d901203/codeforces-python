t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    result = float("inf")
    for i in range(1, n):
        result = min(result, a[i] - a[i - 1])
    print(result)
