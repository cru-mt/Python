def sum_seq(sequence):
    result = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            result += sum_seq(item)
        else:
            result += item
    return result
\