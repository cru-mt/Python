while True:
    x = input()
    if x == "stop":
        break
    else:
        try:
            x = float(x)
            print(x, x ** 3)
        except ValueError:
            print("Podano napis")