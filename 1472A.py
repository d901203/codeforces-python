t = int(input())
for _ in range(t):
    w, h, n = map(int, input().split())
    result = 1
    while result < n:
        if w % 2 == 0:
            w /= 2
            result *= 2
        elif h % 2 == 0:
            h /= 2
            result *= 2
        else:
            break
    if result >= n:
        print("YES")
    else:
        print("NO")
