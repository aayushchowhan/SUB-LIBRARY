from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.properties import StringProperty ,NumericProperty
from kivymd.uix.behaviors import RectangularElevationBehavior
from kivymd.uix.button import MDFillRoundFlatButton
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from client import RequestUtil
req_util = RequestUtil()
class Book:
    def __init__(self,quantity,author,title,edition,pub,year):
        self.title=title
        self.author=author
        self.quantity=quantity
        self.edition=edition
        self.pub= pub
        self.year=year
class Listi(BoxLayout):
    title=StringProperty()
    author=StringProperty()
    quantity=NumericProperty()
    edition=StringProperty()
    pub= StringProperty()
    year=NumericProperty ()
    def add(self,quantity,author,title,edition,pub,year):
        self.title=title
        self.author=author
        self.quantity=quantity
        self.edition=edition
        self.pub= pub
        self.year=year
class Mbg2(FloatLayout):
    pass
class WisBtn(MDFillRoundFlatButton,RectangularElevationBehavior):
    pass
class Search(Screen):
    pass
