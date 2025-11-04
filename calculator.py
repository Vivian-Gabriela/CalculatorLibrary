def add(first_term, second_term):
    return first_term + second_term


def subtract(first_term, second_term):
    return first_term - second_term


def multiply(first_term, second_term):
    return first_term * second_term

def division(first_term, second_term):
    if second_term == 0:
        return "Error: Division by zero"
    resultado = first_term / second_term

    return round(resultado, 2)
