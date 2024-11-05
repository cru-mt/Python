def odwracanie(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1
    return L

#w tym przypadku funkcja iteracyjna jest bardzo prosta i optymalna, nie ma potrzeby wywoływać rekurencji
