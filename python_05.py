variable_a = input("Ingrese a:")
print(variable_a)

variable_b = input("Ingrese b:")
print(variable_b)

variable_a = int(variable_a)
variable_b = int(variable_b)


def sumar(variable_a: int, variable_b: int):
    print(f"OPERACION SUMA: {variable_a} + {variable_b}")
    return variable_a + variable_b


print(f"RESULTADO DE LA SUMA: {sumar(variable_a, variable_b)}")


def restar(variable_a: int, variable_b: int):
    print(f"OPERACION RESTA: {variable_a} - {variable_b}")
    return variable_a - variable_b


print(f"RESULTADO DE LA RESTA: {restar(variable_a, variable_b)}")


def multiplicar(variable_a: int, variable_b: int):
    print(f"OPERACION MULTIPLICACION: {variable_a} * {variable_b}")
    return variable_a * variable_b


print(f"RESULTADO DE LA MULTIPLICACION: {multiplicar(variable_a, variable_b)}")


def dividir(variable_a: int, variable_b: int):
    print(f"OPERACION DIVISION: {variable_a} / {variable_b}")
    return variable_a / variable_b


print(f"RESULTADO DE LA DIVISION: {dividir(variable_a, variable_b)}")


def conversion(variable_a: float, variable_b: float):
    print(f"CONVERSION A FLOTANTE: {variable_a} y {variable_b}")
    return float(variable_a), float(variable_b)


print(f'RESULTADO DE LA CONVERSION: {conversion(variable_a, variable_b)}')


conversionTemperatura = input("Ingrese la temperatura en grados Celsius:")
print(conversionTemperatura)


def conversionTemperatura(variable_a: float, variable_b: float):
    print(f"CONVERSION A FLOTANTE: {variable_a} y {variable_b}")
    return float(variable_a), float(variable_b)