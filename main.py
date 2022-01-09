from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_string("""
<MenuScreen>:
    FloatLayout:
        GridLayout:
            rows: 1
            pos_hint: {"top": 1, "left": 1}
            size_hint: 1, .1
            Button:
                text: "hello world"
        GridLayout:
            rows: 1
            pos_hint: {"top": .9, "left": 1}
            size_hint: 1, .2
   
""")
class MenuScreen(Screen):
    pass
class TestApp(App):

    def build(self):
        return MenuScreen()
if __name__ == "__main__":
    TestApp().run()
