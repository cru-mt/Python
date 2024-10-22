def firstLetters(line):
    words = line.split()
    finalWord = ""
    for word in words:
        finalWord += word[0]

    return finalWord

def lastLetters(line):
    words = line.split()
    finalWord = ""
    for word in words:
        finalWord += word[-1]

    return finalWord

line = "\n ladsddasde   igsadfggn nadsfsafei eesadaeal\n "
print(firstLetters(line))
print(lastLetters(line))