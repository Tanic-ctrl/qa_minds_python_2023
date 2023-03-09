# Ejercicio Operadores
num_a = input("Numero A:")
num_b = input("Numero B:")
num_a = int(num_a)
num_b = int(num_b)

suma = num_a + num_b
resta = num_a - num_b
multiplicacion = num_a * num_b
division = num_a // num_b  # division entera, porque la convierte al numero entero mas cercano
resto_division = num_a % num_b

print(70 * "-")
# Formateo de cadena
print(f"Suma:{suma}")
print(f"Resta:{resta}")
print(f"Multiplicacion:{multiplicacion}")
print(f"Division:{division}")
print(f"Resto division:{resto_division}")
print(70 * "-")

# Ejercicio asignacion de operadores
num_a = input("Ingrese un numero entero:")
num_b = input("Ingrese otro numero entero:")
num_a = int(num_a)
num_b = int(num_b)

# LOGICA, aqui se muestra otra manera de hacer
# el formateo de cadena directamente
print(f"Numero A > Numero B: {num_a > num_b}")
print(f"Numero A < Numero B: {num_a < num_b}")
print(f"Numero A == Numero B: {num_a == num_b}")
print(f"Numero A != Numero B: {num_a != num_b}")
