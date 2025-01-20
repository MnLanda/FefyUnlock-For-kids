import time

def start_timer(duration):
    print(f"Temporizador iniciado por {duration} segundos.")
    time.sleep(duration)
    print("¡El tiempo ha terminado!")