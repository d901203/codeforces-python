n, k = map(int, input().split())
a = list(map(int, input().split()))
print(len([c for c in a if c + k <= 5]) // 3)
