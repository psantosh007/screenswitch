from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

Builder.load_string("""
<CusButton@Button>:
    font_size: 40
    
<CusText@TextInput>:
    font_size: 35
    multiline: False
    
<MenuScreen>:
    id: twonumcal
    display: result
    rows: 2
    padding: 10
    spacing: 10
    
    BoxLayout:
        CusText:
            id: fno
        CusText:
            id: sno
        Label:
            text: '='
            font_size: 40
        CusText:
            id: result
    
    BoxLayout:
        CusButton:
            text: "+"
        CusButton:
            text: "-"
        CusButton:
            text: "x"
               
   
""")
class MenuScreen(Screen):
    pass
class TestApp(App):

    def build(self):
        return MenuScreen()
if __name__ == "__main__":
    TestApp().run()
