def longestWord(line):
    words = line.split()
    word = max(words, key=len)

    return word, len(word)

line = "\n\n 1234  56   \n789 \n"

word, length = longestWord(line)
print("word:", word, "length:",  length)