import sys
import string
import random
#EJERCICIO 1 FUNCIONES
def chequearZen(zen_text, vocales):
    for linea in zen_text:
        palabras = linea.split()[1]
        if(len(palabras) > 1):
            if palabras.startswith(vocales):
                print(linea)
#EJERCICIO 2 FUNCIONES
def maximoTitle(titles, longitud_titles):
    max_len = 0
    for i in range(longitud_titles):
        if(len(titles[i]) > max_len):
            max_len = len(titles[i])
            max_title = titles[i]

    return max_title
#EJERCICIO 4 FUNCIONES
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

#EJERCICIO 7 FUNCIONES
def generarClave(usuario, fecha_actual):
    letras = string.ascii_letters
    numeros = string.digits
    clave_base = usuario + "-" + fecha_actual + "-"
    while (len(clave_base) < 30):
        randomClave = random.choice(letras + numeros)
        clave_base += randomClave
    return clave_base
#EJERCICIO 9 FUNCIONES.
def unirPalabras(clientes):
    listaUnida = [" ".join(cliente.split())for cliente in clientes if cliente is not None and cliente.strip()!=""]
    return listaUnida

def convertirAtitulo(lista_clientes):
    for cliente in lista_clientes:
        lista_clientes[lista_clientes.index(cliente)] = cliente.title()
    return lista_clientes

def eliminarRepetidos(lista_clientes):
    lista_sin_repetidos = list(set(lista_clientes))
    return lista_sin_repetidos

#EJERCICIO 10 FUNCIONES
def insertarRonda(ronda, rounds, ranking_final, acciones):
    maxKills = 0
    maxKillsPlayer = ""
    ronda = ronda-1
    for elem in rounds[ronda]:
        ranking_final[elem]["kills"] += rounds[ronda][elem]["kills"]
        ranking_final[elem]["asistencias"] += rounds[ronda][elem]["assists"]
        if rounds[ronda][elem]["deaths"] == True:
            ranking_final[elem]["muertes"] += 1
        else:
            ranking_final[elem]["muertes"] += 0
        if(rounds[ronda][elem]["kills"] > maxKills):
            maxKills = rounds[ronda][elem]["kills"]
            maxKillsPlayer = elem
    ranking_final[maxKillsPlayer]["mvps"] += 1
    for elemento in ranking_final:
        if ranking_final[elemento]["kills"] > 0:
            ranking_final[elemento]["puntos"] += (ranking_final[elemento]["kills"] * acciones["kill"]) + (ranking_final[elemento]["asistencias"] * acciones["asistencia"]) + (ranking_final[elemento]["muertes"] * acciones["muerte"])
        else:
            ranking_final[elemento]["puntos"] += 0

    return ranking_final
def inicializarRonda():
    ranking_final = {
    "Shadow": {"kills": 0, "asistencias": 0, "muertes": 0, "mvps": 0, "puntos": 0},
    "Blaze": {"kills": 0, "asistencias": 0, "muertes": 0, "mvps": 0, "puntos": 0},
    "Viper": {"kills": 0, "asistencias": 0, "muertes": 0, "mvps": 0, "puntos": 0},
    "Frost": {"kills": 0, "asistencias": 0, "muertes": 0, "mvps": 0, "puntos": 0},
    "Reaper": {"kills": 0, "asistencias": 0, "muertes": 0, "mvps": 0, "puntos": 0},
    }
    return ranking_final

def imprimir_ranking(ranking_final):
    print("{:<10} {:<6} {:<10} {:<8} {:<5} {:<7}".format("Jugador", "Kills", "Asistencias", "Muertes", "MVPs", "Puntos"))
    print("-" * 50)
    
    for jugador, stats in sorted(ranking_final.items(), key=lambda x: x[1]['puntos'], reverse=True):
        print("{:<10} {:<6} {:<10} {:<8} {:<5} {:<7}".format(
            jugador, stats['kills'], stats['asistencias'], stats['muertes'], stats.get('mvps', 0), stats['puntos']
            ))