t = int(input())
for _ in range(t):
    a = list(map(int, input().split()))
    b = sorted(a)[-2:]
    c = [max(a[0], a[1]), max(a[-2], a[-1])]
    if sorted(c) == b:
        print("YES")
    else:
        print("NO")
