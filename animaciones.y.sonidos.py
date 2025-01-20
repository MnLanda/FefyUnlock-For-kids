from kivy.uix.widget import Widget
from kivy.animation import Animation
from kivy.core.audio import SoundLoader

class MyWidget(Widget):
    def animate(self):
        anim = Animation(x=100, y=100, duration=1)
        anim.start(self)



sound = SoundLoader.load('success.mp3')
if sound:
    sound.play()