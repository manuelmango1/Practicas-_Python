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