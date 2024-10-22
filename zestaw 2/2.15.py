def makeString(L):
    stringList = [str(x) for x in L]
    return ''.join(stringList)


L = [12, 3, 456, 7, 891011, 1213]
print(makeString(L))
