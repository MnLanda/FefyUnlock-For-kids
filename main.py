from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window

# Ajustamos el tamaño de la ventana para simular un teléfono móvil
Window.size = (360, 640)  # Tamaño aproximado de un teléfono móvil estándar

class MiApp(App):
    def build(self):
        self.layout = FloatLayout()  # Usamos FloatLayout para organizar los elementos

        # Botón para iniciar el quiz
        self.btn = Button(
            text="Iniciar Quiz",
            font_size=20,
            size_hint=(0.5, 0.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.btn.bind(on_press=self.iniciar_quiz)
        self.layout.add_widget(self.btn)

        # Temporizador en la esquina superior derecha
        self.contador_label = Label(
            text="10",
            font_size=24,
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={'right': 0.95, 'top': 0.95}
        )
        self.layout.add_widget(self.contador_label)

        return self.layout

    def iniciar_quiz(self, instance):
        self.btn.disabled = True  # Desactivar el botón
        self.segundos_restantes = 10  # Tiempo del temporizador
        self.contador_label.text = str(self.segundos_restantes)

        # Mostrar la ecuación centrada
        self.ecuacion_label = Label(
            text="¿Cuánto es 5 + 3?",
            font_size=22,
            size_hint=(None, None),
            pos_hint={'center_x': 0.5, 'center_y': 0.7}
        )
        self.layout.add_widget(self.ecuacion_label)

        # Caja de texto debajo de la ecuación
        self.input_respuesta = TextInput(
            font_size=18,
            size_hint=(0.5, None),
            height=40,
            pos_hint={'center_x': 0.5, 'center_y': 0.6},
            multiline=False,
            hint_text="Escribe tu respuesta"
        )
        self.input_respuesta.max_length = 3  # Limitar a 3 caracteres
        self.layout.add_widget(self.input_respuesta)

        # Botón "Enviar Respuesta" debajo de la caja de texto
        self.btn_enviar = Button(
            text="Enviar Respuesta",
            font_size=18,
            size_hint=(0.5, 0.1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.btn_enviar.bind(on_press=self.validar_respuesta)
        self.layout.add_widget(self.btn_enviar)

        # Iniciar el contador
        self.contador = Clock.schedule_interval(self.contador_temporizador, 1)

    def contador_temporizador(self, dt):
        self.segundos_restantes -= 1
        self.contador_label.text = str(self.segundos_restantes)

        if self.segundos_restantes == 0:
            self.terminar_quiz("Tiempo agotado")

    def validar_respuesta(self, instance):
        respuesta_usuario = self.input_respuesta.text
        if respuesta_usuario.isdigit():
            if int(respuesta_usuario) == 8:
                self.terminar_quiz("¡Correcto! Puedes seguir usando tu celular.")
            else:
                self.input_respuesta.text = ""  # Limpiar el campo para intentar nuevamente
        else:
            self.input_respuesta.text = ""  # Limpiar el campo para entradas no válidas

    def terminar_quiz(self, mensaje):
        self.layout.clear_widgets()  # Limpiar widgets actuales

        # Mostrar mensaje de resultado
        self.resultado_label = Label(
            text=mensaje,
            font_size=18,
            size_hint=(None, None),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.layout.add_widget(self.resultado_label)

        # Detener el temporizador
        Clock.unschedule(self.contador)

        # Volver a mostrar el botón de inicio después de 2 segundos
        Clock.schedule_once(self.mostrar_boton_iniciar, 2)

    def mostrar_boton_iniciar(self, dt):
        self.layout.clear_widgets()
        self.layout.add_widget(self.btn)  # Mostrar el botón de inicio
        self.layout.add_widget(self.contador_label)

if __name__ == '__main__':
    MiApp().run()