t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    visited = set()
    for i, x in enumerate(s):
        if i and s[i - 1] != x and x in visited:
            print("NO")
            break
        visited.add(x)
    else:
        print("YES")
