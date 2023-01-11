from kivy.clock import Clock
from kivy.uix.floatlayout import FloatLayout  
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, BooleanProperty
from kivy.properties import ListProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.carousel import Carousel
from kivy.uix.relativelayout import RelativeLayout
from kivymd.uix.textfield import MDTextFieldRound
from client import RequestUtil
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.behaviors import (
    RectangularRippleBehavior,
    BackgroundColorBehavior,
    RectangularElevationBehavior,)
req_util = RequestUtil()
pre_slide=0
class RectangularElevationButton(
    RectangularRippleBehavior,
    ButtonBehavior,
    RectangularElevationBehavior,
    BackgroundColorBehavior,
):
    md_bg_color = [233/255, 242/255, 235/255, 0]
class Signin_signup(FloatLayout):
    pass
class Page(BoxLayout):
    img=StringProperty()
class Spages(Carousel):
    def  __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.direction="right"
        self.page1=Page(img="imgs/login/1pg_log.png")
        self.page2=Page(img="imgs/login/2pg_log.png")
        self.page3=Signin_signup()
        self.add_widget(self.page1)
        self.add_widget(self.page2)
        self.add_widget(self.page3)
    def show(self):
        global pre_slide
        cur=self.current_slide
        if pre_slide!=cur:
            print(cur)
            pre_slide=cur
class Stater(Screen):
    def  __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.main = BoxLayout()
        self.sp=Spages()
        self.main.add_widget(self.sp)
        self.ind=Indigator(pos_hint={"bottom":1,"center_x":.9},
        size_hint=(1,.3),ci1= [235/255,109/255,156/255,1],
        ci2=[.5,.5,.5,1],ci3=[.5,.5,.5,1])
        self.add_widget(self.main)
        self.add_widget(self.ind)
class ForPassScreen(Screen):
    time = StringProperty()
    total_time=120
    def start_timer(self):
        Clock.schedule_interval(self.timer,1)
    def timer(self,dt):
        self.total_time-=1
        self.time="0"+str(int(self.total_time/60))+" : "+str(self.total_time%60)
        if self.total_time==0:
            return False
class MeraButton(MDTextFieldRound):
    pass
class ChangePassScreen(Screen):
    pass
class Indigator(FloatLayout):
    ci1=ListProperty()
    ci2=ListProperty()
    ci3=ListProperty()
    def change(self,index):
        if 1==index:
            self.ci1=[.5,.5,.5,1]
            self.ci2= [235/255,109/255,156/255,1]
            self.ci3=[.5,.5,.5,1]
        if 2==index:
            self.ci1=[.5,.5,.5,1]
            self.ci2=[.5,.5,.5,1]
            self.ci3= [235/255,109/255,156/255,1]
        if 0==index:
            self.ci1= [235/255,109/255,156/255,1]
            self.ci2=[.5,.5,.5,1]
            self.ci3=[.5,.5,.5,1]
class SignScreen(Screen):
    def check_enrollment(self, enrollment_no):
        response = req_util.make_get_request(ENDPOINT_ROUTE="ask/enrollment",token=enrollment_no)
        print(response)
        return response
    def login_me(self,enrollment_no,password):
        response = req_util.make_post_request(ENDPOINT_ROUTE="token", data={"username":enrollment_no, "password": password})
        if response:
            self.manager.current="nav"
        return response
class ClickableTextFieldRound(RelativeLayout):
    text = StringProperty()
    hint_text = StringProperty()
    passr = BooleanProperty()
