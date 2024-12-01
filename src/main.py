from kivymd.app import MDApp

from kivy.uix.boxlayout import BoxLayout

from kivy.lang.builder import Builder
from kivy.core.window import Window

Window.size = (1080/3, 1920/3)

class Main(MDApp):
    def build(self):
        self.title = "Peger"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Navy"
        return Builder.load_file("main.kv")
    def screen(self, name_screen):
        self.root.ids.screen_manager = name_screen
if __name__ == "__main__":
    Main().run()