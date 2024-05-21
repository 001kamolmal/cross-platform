from kivy.app import App
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager,Screen

class UI(ScreenManager):
    pass

class Logo_page(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        Clock.schedule_once(self.go_to_screen, 3)

    def go_to_screen(self,sec):
        self.manager.current = "Page1"



class Page1(Screen):
    count =0
    def __init__(self, **kw):
        super().__init__(**kw)
        Clock.schedule_interval(self.update_label, 2)

    def update_label(self,num):
        self.count+=1
        self.ids.lbl_count.text = str(self.count)

class clockApp(App):
    def build(self):
        return UI()
    
if __name__ == "__main__":
    clockApp().run()  
    
