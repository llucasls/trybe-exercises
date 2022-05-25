def triangle(side_a, side_b, side_c):
    equal_sides = 0
    sum_a = side_b + side_c
    sum_b = side_a + side_c
    sum_c = side_a + side_b
    if (side_a == side_b):
        equal_sides += 1
    if (side_a == side_c):
        equal_sides += 1
    if (side_b == side_c):
        equal_sides += 1
    if (sum_a <= side_a or sum_b <= side_b or sum_c <= side_c):
        return "não é triângulo"
    elif equal_sides == 1:
        return "Triângulo Isósceles"
    elif equal_sides == 3:
        return "Triângulo Equilátero"
    else:
        return "Triângulo Escaleno"
