v = {"a", "o", "y", "e", "u", "i"}
s = input().lower()
result = ""
for c in s:
    if c in v:
        continue
    else:
        result += "." + c
print(result)
