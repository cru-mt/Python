def printUnderscore(word):
    for i in range(0, len(word) - 1):
        print(word[i], end="_")
    print(word[-1])

word = "word"
printUnderscore(word)