n = int(input())
result = 0
a = {
    "Tetrahedron": 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron": 20,
}
for _ in range(n):
    s = input()
    result += a[s]
print(result)
