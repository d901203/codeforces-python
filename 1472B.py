from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    if total % 2:
        print("NO")
    else:
        c = Counter(a)
        if c[1] % 2:
            print("NO")
        elif c[2] % 2 and c[1] < 2:
            print("NO")
        else:
            print("YES")
