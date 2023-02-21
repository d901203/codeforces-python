s = input()
c = sum(1 if c.isupper() else 0 for c in s)
if c > len(s) - c:
    print(s.upper())
else:
    print(s.lower())
