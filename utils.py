import time

# Función para formatear el tiempo en un formato más amigable
def format_time(seconds):
    """
    Convierte una cantidad de segundos en un formato de minutos:segundos.
    Ejemplo: 130 segundos -> '02:10'.
    """
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02}:{seconds:02}"

# Función que pausa la ejecución durante un tiempo y muestra un mensaje
def delay(seconds, message="Esperando..."):
    """
    Pausa la ejecución por un tiempo determinado.
    """
    print(message)
    time.sleep(seconds)
    print(f"{message} finalizado.")

# Función para mostrar una pregunta del quiz
def ask_question(question, correct_answer):
    """
    Muestra una pregunta y verifica si la respuesta es correcta.
    """
    respuesta = input(question + " ")
    return respuesta == correct_answer