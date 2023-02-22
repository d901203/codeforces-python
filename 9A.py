y, w = map(int, input().split())
a = 6 - max(y, w) + 1


def gcd(a, b):
    return a if not b else gcd(b, a % b)


g = gcd(a, 6)
print(f"{a // g}/{6 // g}")
