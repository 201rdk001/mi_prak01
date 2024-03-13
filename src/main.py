"""Example module providing the user interface for the game."""

from kivy import Config
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout

Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '200')
Config.set('graphics', 'minimum_width', '400')
Config.set('graphics', 'minimum_height', '200')
# Config.set('graphics', 'resizable', False)

class MainGameLayout(BoxLayout):
    """Main layout containing all game widgets/controls"""


class MainWindow(App):
    """Main window of the game"""

    def build(self):
        Builder.load_file("main.kv")

        return MainGameLayout()


if __name__ == '__main__':
    MainWindow().run()
