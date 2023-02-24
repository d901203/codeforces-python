t = int(input())
for _ in range(t):
    m, s = map(int, input().split())
    print(24 * 60 - (m * 60 + s))
