# Ejercicio 16022023

month = input("Please select a month between 1-12:")
month = int(month)

if 0 < month <= 2:
    print("Invierno")
elif month <= 5:
    print("Primavera")
elif month <= 8:
    print("Verano")
elif month <= 11:
    print("Otono")
elif month == 12:
    print("Invierno")
else:
    print("Invalido")

# Ejercicio con operador lógico AND
num_a = 5
num_b = 10
num_c = 12

# Expresion 1: num_c > num_a = True
# Expresion 2: num_c > num_b = False
# True and False: False
if num_c > num_a and num_c > num_b:
    print("C es mayor a A y B")
else:
    print("C no es mayor A y B")

