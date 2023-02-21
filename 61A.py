a = input()
b = input()
result = ["1" if c != d else "0" for c, d in zip(a, b)]
print(*result, sep="")
