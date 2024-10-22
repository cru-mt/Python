def AlphabeticSort(line):
    return ' '.join(sorted(line.split()))

def LengthSort(line):
    return ' '.join(sorted(line.split(), key=len))


line = "Mateusz Ala Klaudia Aleksandra"
print(AlphabeticSort(line))
print(LengthSort(line))