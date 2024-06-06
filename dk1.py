from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from ins import *

class Main(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        lineV = FloatLayout(size_hint=(1,1))
        line1 = BoxLayout(size_hint=(1,0.4),pos_hint= {'y': 0.7, 'center_x':0.5})
        line2 = BoxLayout(size_hint=(0.5,0.05),pos_hint= {'y': 0.4, 'center_x':0.5})
        line3 = BoxLayout(size_hint=(0.5,0.05),pos_hint= {'y': 0.2, 'center_x':0.5})
        line4 = BoxLayout(size_hint=(0.25,0.1),pos_hint= {'y': 0, 'center_x':0.5})

        lab1 = Label(text=inst, color="yellow")
        line1.add_widget(lab1)

        lab2 = Label(text="Введіть ім'я ")
        name = TextInput(multiline=False)
        line2.add_widget(lab2)
        line2.add_widget(name)


        lab3 = Label(text="Введіть вік ")
        age = TextInput(multiline=False)
        line3.add_widget(lab3)
        line3.add_widget(age)

        but1 = Button(text="Почати")
        line4.add_widget(but1)
        
        lineV.add_widget(line1)
        lineV.add_widget(line2)
        lineV.add_widget(line3)
        lineV.add_widget(line4)

        self.add_widget(lineV)



    def next_win(self):
            
            self.manager.current = 'first'
            self.manager.transition.direction = "up"
            

class Win(App):
    def build(self):
        Window.size = (400, 600)
        Window.clearcolor= (1, 1, 0, 1) 
        main_screen= ScreenManager()
        main_screen.add_widget(Main(name='main'))
        return main_screen

app = Win()
app.run()