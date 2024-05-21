from kivy.app import App
from kivy.uix.screenmanager import ScreenManager,Screen


class UI(Screen):
    def add_item(selfe):
        #นำค่าที่พิมพ์ผ่าน textinput ผ่าน spinner
        selfe.ids.spin_lang.values.append(selfe.ids.txt_input.text)

class spinnerApp(App):
    def build(self):
        return UI()
    

if __name__ == "__main__":
    spinnerApp().run()  
    