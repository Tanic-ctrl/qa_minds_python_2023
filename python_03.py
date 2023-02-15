nombre = input("¿Cuál es tu nombre?")
print(nombre)

edad = input("¿Qué edad tiene?")
print(edad)

ciudad = input("¿Cuál es tu ciudad?")
print(ciudad)

estadoCivil = input("¿Está casad@?")
print(estadoCivil)

rangoA = input("Ingrese un número del 1 al 100:")
print(rangoA)
num1 = int(rangoA)

rangoB = input("Ingrese un número del 100 al 200:")
print(rangoB)
num2 = int(rangoB)

resultadoDivision = num1 // num2

print(f'Mi nombre es:{nombre}, mi edad es: {edad}, soy de la ciudad de {ciudad} y mi resultado es: {resultadoDivision}')
