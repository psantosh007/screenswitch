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
    rows: 3
    padding: 10
    spacing: 10
    
    canvas.before:
        Color:
            rgba: (1, 1, 1, 1)
        Rectangle:
            source:'back.jpg'
            size: root.width, root.height
            pos: self.pos
    BoxLayout:
        rows: 1
        pos_hint: {"top": 1,"left": 1}
        size_hint: 1, .1
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
        rows: 1
        pos_hint: {"top": .9,"left": 1}
        size_hint: 1, .1
        CusButton:
            text: "+"
        CusButton:
            text: "-"
        CusButton:
            text: "x"
    ScrollView:
        pos_hint: {"top": .8,"left": 1}
        size_hint: 1, .5
        do_scroll_x: False
        Label:
            id: viewout
            size_hint: None, None
            size: self.texture_size  
            text: " scroll view " * 20        
   
""")
class MenuScreen(Screen):
    pass
class TestApp(App):

    def build(self):
        return MenuScreen()
if __name__ == "__main__":
    TestApp().run()
