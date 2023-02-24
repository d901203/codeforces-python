n, m = map(int, input().split())


def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


i = n + 1
while not is_prime(i):
    i += 1
if i == m:
    print("YES")
else:
    print("NO")
