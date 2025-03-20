import sys
import random
import string
# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]
# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
    "// Esto es un comentario",
    "/* Esto es un comentario */",
    "-- Esto es un comentario",
    "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]
# Índice de la respuesta correcta para cada pregunta, el el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]
#CREO EL PUNTAJE DE LOS JUGADORES.
players_score = 0
#TRAIGO LOS NUMEROS
numbers = string.digits
#A continuacion, creo la variable questions_to_ask, lo que sera una tupla con pregunta, respuesta e indice de respuesta correcta.
questions_data = list(zip(questions,answers,correct_answers_index))
#Selecciono 3 tuplas aleatorias
questions_to_ask = random.sample(questions_data, k = 3) #unicamente cambio por random.sample para que no se repita
# El usuario deberá contestar 3 preguntas
for question, answers, correct_answers_index in questions_to_ask:
    print(question) #imprimo la pregunta aleatoria
    #question_index = random.randint(0, len(questions) - 1) : deshice esta linea ya que la pregunta random la seleccionamos con random.choices
    # Se muestra la pregunta y las respuestas posibles
    #print(questions[question_index]) #deshice esta linea, ya que la seleccion aleatoria la hicimos.
    for i, answer in enumerate(answers):
        print(f"{i + 1}. {answer}")
    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = input("Respuesta: ")
        # Se verifica si la respuesta es correcta
        if user_answer in numbers:
            user_answer = int(user_answer) - 1
            if user_answer == correct_answers_index:
                print("¡Correcto!")
                players_score = players_score + 1
                break
            elif user_answer not in range(4):
                print('Numero no valido')
                sys.exit(1)
            else:
                players_score = players_score - 0.5
        else:
            print('Respuesta no valida')
            sys.exit(1)
    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(answers[correct_answers_index])
    # Se imprime un blanco al final de la pregunta
    print()
print(f'el score conseguido por el participante es de {players_score}')
