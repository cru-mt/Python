def fibonacci(n): #za pierwszy wyraz przyjmuję 1
    a, b = 1, 1
    if n < 3:
        return 1
    for i in range(2, n):
        if a < b:
            a = a + b
        else:
            b = a + b

    return max(a, b)
