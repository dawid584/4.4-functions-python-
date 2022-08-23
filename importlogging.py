import logging

logging.basicConfig(level=logging.INFO)

def sum(a, b, *args):
    logging.info(f"Dodaję {a} i {b}")
    sum_1 = a + b
    return sum_1
    

def sub(a, b, *args):
    logging.info(f"Dodaję {a} i {b}")
    sub_1 = a + b
    return sub_1

def mul(a, b, *args):
    logging.info(f"Dodaję {a} i {b}")
    mul_1 = a + b
    return mul_1

def div(a, b, *args):
    logging.info(f"Dodaję {a} i {b}")
    div_1 = a + b
    return div_1
    def get_data():
    operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie:")
    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę: "))
    
    if type(a) ==(int) or type(a) ==(float) :
        logging.info(f"argument {a} jest liczbą")
    else:
        logging.info(f"argument {a} nie jest liczbą")

    
    if type(b) ==(int) or type(b) == (float):
        logging.info(f"argument {b} jest liczbą")
    else:
        logging.info(f"argument {b} nie jest liczbą")
    # dalej pobierasz argumenty i sprawdzasz czy są liczbami
    # te args w prostszej wersji możesz sobie darować.

    return operation, a, b

