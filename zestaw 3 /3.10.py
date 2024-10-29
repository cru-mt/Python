def roman2int(x):
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    sum = 0
    x = x.upper()
    if len(x) == 1:
        if x not in roman:
            raise ValueError('Invalid Roman numeral')
        return roman[x]

    for i in range(0, len(x) - 1):
        if x[i] not in roman:
            raise ValueError('Invalid Roman numeral')
        if roman[x[i]] < roman[x[i + 1]]:
            sum += roman[x[i + 1]] - roman[x[i]]
            i += 1
        else:
            sum += roman[x[i]]
            if i == len(x) - 2:
                sum += roman[x[i + 1]]

    return sum


x = input("Cyfra rzymska: ")

try:
    print(roman2int(x))
except ValueError:
    print("Podano nieprawidłową liczbę rzymską")
