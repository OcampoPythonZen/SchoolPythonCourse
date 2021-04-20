"""
Pedir dos numeros , dividor esos dos numeros
y muestre por pantalla si el divisor es cero un error
o avisar que no puede realizar la operacion.
"""


def division(number_one: float, number_two: float) -> float:
    if number_two == 0:
        result = .0
    else:
        result = number_one/number_two
    return result


if __name__ == '__main__':
    number_one = int(input("Dame el divisor"))
    number_two = int(input("Dame el dividendo"))
    print(division(number_one, number_two))
