from kivy.app import App
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        btn = Button(text="¡Empieza el quiz!", font_size=24)
        return btn

if __name__ == '__main__':
    MyApp().run()