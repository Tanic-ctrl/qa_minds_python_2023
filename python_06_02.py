# Escribe un script que dado el día, mes y año de nacimiento de una persona determine lo siguiente:
# Cuántos años tiene.
# Si en lo que va del año ya cumplió o no.
# Determinar a qué generación pertenece:
# La generación silenciosa. Nacidos entre 1920 y 1939.
# Los baby boomers. Nacidos entre 1940 y 1959.
# Generación X. Nacidos entre 1960 y 1979.
# Generación Y o millennials. Nacidos entre 1980 y 1989.
# Generación Z. Nacidos entre 1990 en adelante.
# Extra: Utilizar libreria de datetime para obtener mes y año.

# CONSTANTS
CURRENT_YEAR = 2023
CURRENT_MONTH = 2
CURRENT_DAY = 21

# USER INPUTS
year = input("What year were you born?:")
year = int(year)
month = input("What month were you born?:")
month = int(month)
day = input("What day were you born?:")
day = int(day)

# LOGIC
person_age = CURRENT_YEAR - year
print(f"Your age is {person_age}")

person_birthday = (month >= CURRENT_MONTH) and (day >= CURRENT_DAY)
print(f"Birthday: {person_birthday}")


if year <= 1939:
    print("Silent generation")
elif year <= 1959:
    print("Baby boomers")
elif year <= 1979:
    print("Generation X")
elif year <= 1989:
    print("Generation Y & Millennials")
else:
    print("Generation Z")
