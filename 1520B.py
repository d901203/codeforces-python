t = int(input())
for _ in range(t):
    n = input()
    l = len(n)
    o = int("1" * l)
    print(9 * (l - 1) + int(n) // o)
