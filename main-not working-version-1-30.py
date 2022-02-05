import paho.mqtt.client as mqttClient
import time
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen


Builder.load_string("""
<CusButton@Button>:
    font_size: 40
    
<CusText@TextInput>:
    font_size: 35
    multiline: False
    
<Screen1>:
    name: 'screen1'
    sub_data: sub_data
    canvas.before:
        Color:
            rgba: (1, 1, 1, 1)
        Rectangle:
            source:'back.jpg'
            size: root.width, root.height
            pos: self.pos
    BoxLayout:
        rows: 3
        
        orientation: "vertical"
        pos_hint: {"top": 1,"left": 1}
        size_hint: 1, .4
        CusButton:
            text: "Next"
            on_press: root.manager.current = 'screen2'
        CusButton:
            text: "SUBSCRIBE"
            on_press: root.mqtt_subscribe()
            
        CusText:
            id: server_id
            hint_text: "Write Server name"
        CusText:
            id: subscription_id
            hint_text: "Write Subscrption ID"
        Label:
            id: sub_data
            text: "GeeksForGeeks \\n is the best platform for DSA content"
            
        
                              
<Screen2>:
    name: 'screen2'
    canvas.before:
        Color:
            rgba: (1, 1, 1, 1)
        Rectangle:
            source:'back.jpg'
            size: root.width, root.height
            pos: self.pos
    BoxLayout:
        CusButton:
            text: "Previous"
            pos_hint: {"top": 0.1, "left": 0.5}
            size_hint: .1, .1 
            on_press: root.manager.current = 'screen1'
""")

class Screen1(Screen):
    
    sub_data=ObjectProperty()

    def mqtt_subscribe(self):
        
        
        
#        a = "ff"  
#        b="cc"  
#        c="ff"
#        sam=[a,b,c]

 #       sam_comb= "\n".join(sam)
        sam_comb="Nathan Paonam"
        self.sub_data.text= sam_comb

        
  #      broker_address= "test.mosquitto.org"  #Broker address
  #      port = 1883                         #Broker port
  #      user = "yourUser"                    #Connection username
  #      password = "yourPassword"            #Connection password
  #        
  #      client = mqttClient.Client("Python")               #create new instance
  #    
  #      client.connect(broker_address, port=port)          #connect to broker
         
        
class Screen2(Screen):
    pass
            
sm= ScreenManager()
sm.add_widget(Screen1(name='screen1'))
sm.add_widget(Screen2(name='screen2'))

      
class TestApp(App):

    def build(self):
        return sm
         
if __name__ == "__main__":
    TestApp().run()
