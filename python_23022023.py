number = 0
while number < 5:
    print (number)
    number -= 1
    print ('Fin de ejecucion')


#Ejercicio 1
#Escribe un script que dado un numero permita calcular la sumatoria de todos los numeros que lo preceden desde cero.
number = 5
suma = 0
while number > 0:
    suma += 1



#Ejercicio 2
# Escribe un script que dado dos números permita mostrar todos los números que existen entre ambos. Ejemplo:
numero_a = 8
numero_b = 5
#Resultado: 6,7

iterador = numero_a + 1
while numero_a < iterador < numero_b:
    print(iterador)
    iterador +=1


low_limit = min(numero_a, numero_b)
upper_limit = max(numero_a, numero_b)



#Ejercicio 3
#Escribe un script que dado un número aleatorio permita encontrar su valor por medio de interacción con usuario,
# mostrando cuantos intentos le llevó al mismo detectarlo. Para realizar este script será necesario utilizar la
# librería random y del comando input para ingresar el número por consola.