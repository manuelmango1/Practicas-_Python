import sys

def chequearZen(zen_text, vocales):
    for linea in zen_text:
        palabras = linea.split()[1]
        if(len(palabras) > 1):
            if palabras.startswith(vocales):
                print(linea)

def maximoTitle(titles, longitud_titles):
    max_len = 0
    for i in range(longitud_titles):
        if(len(titles[i]) > max_len):
            max_len = len(titles[i])
            max_title = titles[i]

    return max_title

def registrarse(mayus,numeros,validos):
    sumaMayus = 0
    sumaNum = 0
    user_password = input('Ingrese su nombre de usuario: ')
    if(len(user_password) > 4):
        for letra in user_password:
            if letra in mayus:
                sumaMayus += 1
            if letra in numeros:
                sumaNum += 1
        if letra not in validos:
            print('Caracter no valido')
            sys.exit(1)
        if sumaMayus > 0 and sumaNum > 0 :
            print('Usuario registrado')
        if sumaMayus == 0:
            print('Falta mayuscula')
        if sumaNum == 0:
            print('Falta numero')
    else:
        print('El nombre debe contener 5 caracteres como minimo, y sin caracteres especiales (debe contener una mayuscula y un numero)')