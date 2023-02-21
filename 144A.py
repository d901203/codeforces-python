n = int(input())
a = list(map(int, input().split()))
mx = a.index(max(a))
mn = n - 1 - a[::-1].index(min(a))
if mx > mn:
    print(mx + (n - 1 - mn) - 1)
else:
    print(mx + (n - 1 - mn))
