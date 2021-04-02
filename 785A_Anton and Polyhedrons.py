Tetrahedron = 4
Cube = 6
Octahedron = 8
Dodecahedron = 12
Icosahedron = 20

t = int(input())
summ = 0
while t > 0:
    a = input()
    if a == "Tetrahedron":
        summ += 4
    elif a == "Cube":
        summ += 6
    elif a == "Octahedron":
        summ += 8
    elif a == "Dodecahedron":
        summ += 12
    else:
        summ += 20

    t -= 1


print(summ)
