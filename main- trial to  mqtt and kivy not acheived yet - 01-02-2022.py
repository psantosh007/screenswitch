import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.progressbar import ProgressBar
from kivy.properties import ObjectProperty
from kivy.properties import NumericProperty
from kivy.clock import Clock, mainthread
from kivy.garden import knob
from kivy.lang import Builder
#from kivy.garden import gauge
from functools import partial
import paho.mqtt.client as mqtt


Builder.load_string("""
<MyGrid>:
    temp: gauge_1
    hum: gauge_2
    lbl1: lbl1
    lbl2: lbl2
    knob1: knob1
    knob2: knob2
    cols: 2
    GridLayout:
        cols:1
        size: root.size
        size_hint_y: 1
        GridLayout:
            cols:2
            padding: 20
            spacing: 20
            Knob:
                id: knob1
                size: 500, 500
                value: 0
                knobimg_source: "img/knob_metal.png"
                markeroff_color: 0.0, 0.0, .0, 1
                knobimg_size: 0.9
                marker_img: "img/bline3.png"

            Knob:
                id: knob2
                value: 0
                size: 500, 500
                knobimg_source: "img/knob_metal.png"
                markeroff_color: 0.0, 0.0, .0, 1
                knobimg_size: 0.9
                marker_img: "img/bline3.png"

            ProgressBar:
                
                id: gauge_1
                width: 300

            ProgressBar:

                width: 300
                id: gauge_2
            Label:
                font_size:'40sp'
                id: lbl2

            Label:
                font_size:'40sp'    
                id: lbl1

""")



class MyGrid(GridLayout):
    temp = ObjectProperty(None)
    hum = ObjectProperty(None)
    lbl1 = ObjectProperty(None)
    lbl2 = ObjectProperty(None)
    knob1 = ObjectProperty(None)
    knob2 = ObjectProperty(None)

    @mainthread
    def update(self, temp, humid,*a):
        self.temp.value=float(temp)
        self.hum.value=float(humid)
        self.lbl2.text='T: ' + str(temp) + u'\N{DEGREE SIGN}' +'C'    
        self.lbl1.text='H: ' +str(humid) + ' %'
        self.knob2.value=float(humid)
        self.knob1.value=float(temp)

class mainApp(App):
    client = mqtt.Client("P1")
    def on_message(self,client, userdata, message):
        data=message.payload.decode("utf-8").split(':')

        self.root.update(data[0],data[1],1)

    def build(self):
        #client = mqtt.Client("P1") 
        self.client.on_message=self.on_message 
        self.client.connect('192.168.100.19',1883)
        self.client.loop_start()
        self.client.subscribe([("temp_mon/temp",0),("temp_mon/hum",0)])

        return MyGrid()

    def on_pause(self):
        self.client.disconnect()

    def on_resume(self):
        self.client.on_message=self.on_message 
        self.client.connect('192.168.100.19',1883)
        self.client.loop_start()
        self.client.subscribe([("temp_mon/temp",0),("temp_mon/hum",0)])


if __name__ == "__main__":
    mainApp().run()