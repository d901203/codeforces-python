n = int(input())
if n & 1:
    print((n - 3) // 2 + 1)
    print("2 " * ((n - 3) // 2), "3")
else:
    print(n // 2)
    print("2 " * (n // 2))
