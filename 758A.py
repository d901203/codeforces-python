n = int(input())
a = list(map(int, input().split()))
x = max(a)
print(sum(x - c for c in a))
