def my_sqrt(x):
    approx = None
    guess = x / 2

    while approx != guess:
        approx = guess
        guess = (approx + x / approx) / 2

    return approx


def sqrt_program(arg: str) -> None:
    x = int(arg)
    print("The root of", x, "is", my_sqrt(x))


sqrt_program("4")