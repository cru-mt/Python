def charCount(line):
    words = line.split()
    sum = 0
    for word in words:
        sum += len(word)

    return sum

line = "\n\n 1234  56   \n789 \n"
print(charCount(line))