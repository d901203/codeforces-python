from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    for i, x in enumerate(a):
        if c[x] == 1:
            print(i + 1)
            break
