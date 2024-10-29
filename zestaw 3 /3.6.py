def makeRectangle(width, height):
    rectangle = ""
    top = ""
    side = ""
    for i in range(0, width):
        top += "+---"
        side += "|   "
    side += "|\n"
    top += "+\n"

    for i in range(0, height):
        rectangle += top + side

    return rectangle + top


print(makeRectangle(5, 3))