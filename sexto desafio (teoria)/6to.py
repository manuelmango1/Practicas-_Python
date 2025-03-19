#Escribir un programa que ingrese de teclado una cadena de caracteres e imprima cuantas letras "a" contiene.

cadena = input('Ingrese una cadena de caracteres: ')
cadena = cadena.lower()
cantidad_a = 0
for letra in cadena:
    if letra == 'a':
        cantidad_a = cantidad_a + 1

print(f'La cantidad de letras a de la palabra {cadena} es de {cantidad_a}')
