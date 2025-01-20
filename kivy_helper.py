from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        # Cambiar el mensaje de bienvenida a tu preferencia
        return Label(text="Hey, ¿será que puedes responder esto?", font_size=32, color=(1, 0, 0, 1))  # Rojo, tamaño 32

if __name__ == '__main__':
    MyApp().run()