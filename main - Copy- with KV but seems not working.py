from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
# BoxLayout: it's in the python part, so you need to import it
from kivy.lang import Builder
Builder.load_string("""
<MyLayout>
    orientation:"vertical"
    Label: # it's in the kv part, so no need to import it
        id:mylabel
        text:"My App"
    Button:
        text: "Click me!"
        on_press: print("santosh")
""")
class MyLayout(BoxLayout):
    pass
class TutorialApp(App):
    def build(self):
        return MyLayout()
TutorialApp().run()

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.lang import Builder

Builder.load_string("""
<Controller>:
    label_wid: my_custom_label

    BoxLayout:
        orientation: ’vertical’ 
        padding: 20
    Button:
        text: ’My controller info is: ’ + root.info 
        on_press: root.do_action()
    Label:
        id: my_custom_label
        text: ’My label before button press

""")


class Controller(FloatLayout):
    ’’’Create a controller that receives a custom widget from the kv lang file.
    Add an action to be called from the kv lang file. ’’’
    
    label_wid = ObjectProperty()
    info = StringProperty()

    def do_action(self):
        self.label_wid.text = ’My label after button press’
        self.info = ’New info text’

    class ControllerApp(App): 
        def build(self):
            return Controller(info=’Hello world’)
    if __name__ == ’__main__’: 
        ControllerApp().run()