import logging

logging.basicConfig(level=logging.INFO)

def sum(a, b, *args):
    logging.info(f"Dodaję {a} i {b}")
    sum_1 = a + b
    return sum_1
    

def sub(a, b, *args):
    logging.info(f"Dodaję {a} i {b}")
    sub_1 = a - b
    return sub_1

def mul(a, b, *args):
    logging.info(f"Dodaję {a} i {b}")
    mul_1 = a * b
    return mul_1

def div(a, b, *args):
    logging.info(f"Dodaję {a} i {b}")
    div_1 = a / b
    return div_1


def get_data():
    operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę: "))
    

    return operation, a, b


operations = { "1": sum , "2": sub , "3": mul , "4": div}

def main():

    operation, a, b, *args = get_data()
    result = operations[operation](a, b, *args)
    print(f"Wynik to {result}")
  
main()

