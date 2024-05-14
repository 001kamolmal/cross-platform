from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager,Screen

class MainScreen(Screen): # หน้าจอ 1
    pass

class LoginScreen(Screen):
    pass

class UI(ScreenManager): # ทำหน้าที่จัดการหน้าจอต่างๆ
    pass

class Scr1(Screen):
    pass

class Scr2(Screen):
    def convert(self, *args):
        num = int(self.ids.txt_number.text)
        if args[0].text=="base 2":
            self.ids.lbl_output.text = bin(num)[2:]
        elif args[0].text=="base 8":
            self.ids.lbl_output.text = oct(num)[2:]
        elif args[0].text=="base 16":
            self.ids.lbl_output.text = hex(num)[2:]

class convertApp(App):
    def build (self):
        return UI()
    

if __name__=="__main__":   
    convertApp().run()