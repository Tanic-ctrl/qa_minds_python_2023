def sumar(variable_a: int, variable_b: int) -> int:
    """Suma de dos números enteros.

    :param variable_a: Primer número
    :param variable_b: Segundo número
    :return Resultado de sumar primer número + segundo número
    """
    print(f"OPERACION SUMA: {variable_a} + {variable_b}")
    return variable_a + variable_b


def restar(variable_a: int, variable_b: int) -> int:
    """Resta de dos números enteros

    :param variable_a: Primer número
    :param variable_b: Segundo número
    :return: Resultado de restar primer número - segundo número
    """
    print(f"OPERACION RESTA: {variable_a} - {variable_b}")
    return variable_a - variable_b


def multiplicar(variable_a: int, variable_b: int) -> int:
    """Múltiplicación de dos números enteros.

    :param variable_a: Primer número
    :param variable_b: Segundo número
    :return: Resultado de múltiplicar primer número * segundo número
    """
    print(f"OPERACION MULTIPLICACION: {variable_a} * {variable_b}")
    return variable_a * variable_b


def dividir(variable_a: int, variable_b: int) -> int:
    """

    :param variable_a: Primer número
    :param variable_b: Segundo número
    :return: Resultado de dividir primer número / segundo número
    """
    print(f"OPERACION DIVISION: {variable_a} / {variable_b}")
    return variable_a / variable_b


def modulo(variable_a: int, variable_b: int) -> int:
    """

    :param variable_a: Primer número
    :param variable_b: Segundo número
    :return: Resultado de obtener el módulo del primer número entre segundo número
    """
    print(f"OPERACION MODULO: {variable_a} % {variable_b}")
    return variable_a % variable_b


def convertir_entero(var) -> int:
    """Convertir una variable a entero.

    :param var: Valor ingresado
    :return:
    """
    return int(var)


variable_a = input("Ingrese a:")
variable_b = input("Ingrese b:")

variable_a = convertir_entero(variable_a)
variable_b = convertir_entero(variable_b)

print(f"RESULTADO DE LA SUMA: {sumar(variable_a, variable_b)}")
print(f"RESULTADO DE LA RESTA: {restar(variable_a, variable_b)}")
print(f"RESULTADO DE LA MULTIPLICACION: {multiplicar(variable_a, variable_b)}")
print(f"RESULTADO DE LA DIVISION: {dividir(variable_a, variable_b)}")
print(f"RESULTADO DE MODULO: {modulo(variable_a, variable_b)}")

# Ejercicio adicional
grados_celsius = input("Ingrese la temperatura en grados Celsius:")

grados_celsius = int(grados_celsius)


def conversionTemperatura(grados_celsius):
    print(f"CONVERTIR DE GRADOS CELSIUS A FAHRENHEIT: {grados_celsius}C°")
    return (grados_celsius * 1.8) + 32


print(f'RESULTADO DE CONVERTIR GRADOS CELSIUS A FAHRENHEIT: {conversionTemperatura(grados_celsius)}')
