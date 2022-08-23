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

