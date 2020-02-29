# ZADANIE 1.
# GENERATOR KODÓW POCZTOWYCH
# przyjmuje 2 stringi: "79-900" i "80-155" i zwraca listę kodów pomiędzy nimi


def postal_code_generator(start: str, stop: str) -> list:
    start = int(start.replace('-', ''))
    stop = int(stop.replace('-', ''))
    postal_code_list = [f'{str(x)[:2]}-{str(x)[2:]}' for x in range(start, stop + 1)]
    return postal_code_list



