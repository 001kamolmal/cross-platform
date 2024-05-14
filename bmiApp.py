from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.filechooser import Screen

class UI(ScreenManager): # ทำหน้าที่แสดง UI
    pass 

class LoginScreen(Screen): 
    pass

class MainScreen(Screen): # หน้าจอ1
    pass


class bmiApp(App):
    def build(self):
        return UI()
    
if __name__=="__main__":
    bmiApp().run()

