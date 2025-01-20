import random
import time

def start_quiz_timer(duration):
    print(f"Temporizador con quiz iniciado por {duration} segundos.")
    time.sleep(duration)  # Esperar el tiempo del temporizador

    # Generar una pregunta matemática simple
    operacion = random.choice(['+', '-'])
    if operacion == '+':
        num1, num2 = random.randint(1, 10), random.randint(1, 10)
        pregunta = f"¿Cuánto es {num1} + {num2}?"
        respuesta = str(num1 + num2)
    elif operacion == '-':
        num1, num2 = random.randint(10, 30), random.randint(1, 10)
        pregunta = f"¿Cuánto es {num1} - {num2}?"
        respuesta = str(num1 - num2)

    return pregunta, respuesta