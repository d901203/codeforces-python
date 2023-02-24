t = int(input())
for _ in range(t):
    s = input()
    n = len(s) // 2
    if s[:n] * 2 == s:
        print("YES")
    else:
        print("NO")
