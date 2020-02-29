# ZADANIE 3.
# NALEŻY WYGENEROWAĆ LISTĘ LICZB OD 2 DO 5.5 ZE SKOKIEM CO 0.5,
# DANE WYNIKOWE MUSZĄ BYĆ TYPU DECIMAL.


def number_generator(start: float = 2, stop: float = 5.5) -> list:
    start = int(start * 10)
    stop = int(stop * 10)
    number_list = [x / 10 for x in range(start, stop + 1, 5)]
    return number_list



