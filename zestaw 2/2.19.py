def equalString(L):
    stringList = [str(x).zfill(3) for x in L]
    return ' '.join(stringList)


L = [1, 23, 567, 9, 34, 905, 23, 4]
print(equalString(L))