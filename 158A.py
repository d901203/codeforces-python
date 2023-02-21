import bisect

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = a[k - 1]
a.reverse()
if not b:
    print(n - bisect.bisect_right(a, b))
else:
    print(n - bisect.bisect_left(a, b))
