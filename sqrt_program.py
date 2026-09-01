def my_sqrt(x):
    approx = None
    guess = x / 2

    while approx != guess:
        approx = guess
        guess = (approx + x / approx) / 2

    return approx


print(my_sqrt(4))