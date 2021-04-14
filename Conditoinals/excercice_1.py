"""
Realizar in programa que pida la edad
y avise si es mayo de edad o no.
"""


def mayor_de_edad(edad: int) -> str:
    if edad >= 18:
        return "Youre over 18 years old"
    else:
        return "Youre not over 18 years old"


if __name__ == "__main__":
    edad = int(input("Type your age "))
    print(mayor_de_edad(edad))
