def chequearZen(zen_text, vocales):
    for linea in zen_text:
        palabras = linea.split()[1]
        if(len(palabras) > 1):
            if palabras.startswith(vocales):
                print(linea)