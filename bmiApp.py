from kivy .app import App 
from kivy.uix.screenmanager import ScreenManager,Screen

class LoginScreen(Screen): #หน้า 2
    def cal_bmi(self): 
        #ค่า bmi = น้ำหนัก กก / (ส่วนสูง เมตร * น้ำหนัก กก)
        weight = float(self.ids.txt_weight.text)
        height = float(self.ids.txt_height.text)
        height = height/100

        bmi = weight/(height*height) #สูตรการคำนวณ bmiS
        self.ids.lbl_bmi.text=str(bmi)
        if bmi > 35:
            self.ids.lbl_bmi.color="red"
            self.ids.img_bmi.source="pic/5.PNG"
        elif bmi > 30:
            self.ids.lbl_bmi.color="FF6600" #สีส้ม
            self.ids.img_bmi.source="pic/4.PNG"
        elif bmi > 25:
            self.ids.lbl_bmi.color="FFFF33" #สีเหลือง
            self.ids.img_bmi.source="pic/3.PNG"
        elif bmi > 18:
            self.ids.lbl_bmi.color="green"
            self.ids.img_bmi.source="pic/2.PNG"
        else:
            self.ids.lbl_bmi.color="33CCFF" #สีฟ้า
            self.ids.img_bmi.source="pic/1.PNG"

class MainScreen(Screen): # หน้าจอ 1
    pass

class UI(ScreenManager): # ทำหน้าที่จัดการหน้าจอต่างๆ
    pass

class bmiApp(App):
    def build (self):
        return UI()
    
if __name__=="__main_":   
    bmiApp().run()