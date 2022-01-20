
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.lang import Builder
import threading

Builder.load_string('''

<MyBox>:
    orientation: 'horizontal'
    cols: 2
    Label:
        text: root.tobeupd
    Button:
        text: 'Start Update'
        on_release: root.upd_ltxt()

''')

class MyBox(BoxLayout):
    tobeupd = StringProperty()

    def __init__(self,*args,**kwargs):
        super(MyBox,self).__init__(*args,**kwargs)
        self.tobeupd = '#'

    def upd_ltxt(self):
        threading.Thread(target=self.update_label).start()

    def update_label(self):
        for i in range(1,10):
            print(self.tobeupd)
            self.tobeupd = str(i)
            input('Write something: ')  # new line, see edit below



class updApp(App):
    def build(self):
        return MyBox()

if __name__ == '__main__':
    updApp().run()







Button:
    id: updatebutton
    text: 'Start Update'
    on_release: root.upd_ltxt()


def update_label(self):

    self.ids.updatebutton.disabled = True

    for i in range(1,10):
        self.tobeupd = str(i)
        input('Write something: ')

    self.ids.updatebutton.disabled = False
