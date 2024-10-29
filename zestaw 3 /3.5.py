def buildRuler(size):
    ruler = ""
    for i in range(0, size):
        ruler += "|...."
    ruler += "|\n"
    for i in range(0, size + 1):
        ruler += str(i)
        for j in range(0, 5 - len(str(i + 1))):
            ruler += ' '
    return ruler


print(buildRuler(12))