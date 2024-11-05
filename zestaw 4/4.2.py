def make_ruler(n):
    ruler = ""
    for i in range(0, n):
        ruler += "|...."
    ruler += "|\n"
    for i in range(0, n + 1):
        ruler += str(i)
        for j in range(0, 5 - len(str(i + 1))):
            ruler += ' '
    return ruler


def make_grid(rows, cols):
    rectangle = ""
    top = ""
    side = ""
    for i in range(0, rows):
        top += "+---"
        side += "|   "
    side += "|\n"
    top += "+\n"

    for i in range(0, cols):
        rectangle += top + side

    return rectangle + top
