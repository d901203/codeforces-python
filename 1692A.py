t = int(input())
for _ in range(t):
    a = list(map(int, input().split()))
    print(sum(1 if c > a[0] else 0 for c in a[1:]))
