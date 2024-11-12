import math


def correct_frac(frac):
    if frac[0] == 0:
        frac[1] = 0
        return frac

    if frac[0] < 0 and frac[1] < 0:
        frac = [abs(x) for x in frac]

    elif frac[0] > 0 and frac[1] < 0:
        frac = [x * -1 for x in frac]

    gcd = math.gcd(frac[0], frac[1])
    if gcd != 1:
        frac = [x // gcd for x in frac]

    return frac


def add_frac(frac1, frac2):  # frac1 + frac2
    frac1 = correct_frac(frac1)
    frac2 = correct_frac(frac2)

    if is_zero(frac1):
        return frac2
    elif is_zero(frac2):
        return frac1

    lcd = abs(frac1[1] * frac2[1]) // math.gcd(frac1[1], frac2[1])
    frac1[0] = frac1[0] * (lcd // frac1[1])
    frac2[0] = frac2[0] * (lcd // frac2[1])

    return correct_frac([frac1[0] + frac2[0], lcd])


def sub_frac(frac1, frac2):  # frac1 - frac2
    frac1 = correct_frac(frac1)
    frac2 = correct_frac(frac2)

    if is_zero(frac1):
        return [frac2[0] * -1, frac2[1]]
    elif is_zero(frac2):
        return frac1

    lcd = abs(frac1[1] * frac2[1]) // math.gcd(frac1[1], frac2[1])
    frac1[0] = frac1[0] * (lcd // frac1[1])
    frac2[0] = frac2[0] * (lcd // frac2[1])

    return correct_frac([frac1[0] - frac2[0], lcd])


def mul_frac(frac1, frac2):  # frac1 * frac2
    frac1 = correct_frac(frac1)
    frac2 = correct_frac(frac2)
    if is_zero(frac1) or is_zero(frac2):
        return [0, 0]

    return correct_frac([frac1[0] * frac2[0], frac1[1] * frac2[1]])


def div_frac(frac1, frac2):  # frac1 / frac2
    if is_zero(frac2):
        raise ZeroDivisionError
    if is_zero(frac1):
        return [0, 0]

    return mul_frac(frac1, [frac2[1], frac2[0]])


def is_positive(frac):  # bool, czy dodatni
    if correct_frac(frac)[0] < 0:
        return False
    return True


def is_zero(frac):  # bool, typu [0, x]
    if frac[0] == 0:
        return True
    return False


def cmp_frac(frac1, frac2):  # -1 | 0 | +1
    if frac2float(frac1) > frac2float(frac2):
        return 1
    elif correct_frac(frac1) == correct_frac(frac2):
        return 0
    else:
        return -1


def frac2float(frac):  # konwersja do float
    return frac[0] / frac[1]

