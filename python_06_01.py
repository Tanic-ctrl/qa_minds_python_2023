# Escribe un script que dado la edad de una persona y su altura pueda determinar si la misma puede o no subirse
# en la montaña rusa “Push-Pull”, dado que se debe ser mayor a 14 años y tener una altura no menor de 1,62.
# El script debe ser capaz de informar si puede o no subirse y en el caso de que no, porque razón
# (Si por edad, por tamaño u ambas)

# CONSTANTS
# En python las constantes se definen en mayúsculas
AGE_LIMIT = 14
HEIGHT_LIMIT = 1.62

# USER INPUTS
age = input("What is your age?:")
age = int(age)
height = input("What is your height:")
height = float(height)

# LOGIC
valid_age = age > AGE_LIMIT
valid_height = height > HEIGHT_LIMIT

if valid_height and valid_height:
    print(f"You can aboard")
else:
    print(f"You cannot aboard because the valid age is {valid_age} and the valid height is {valid_height}")
