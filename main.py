from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivymd.app import MDApp
from kivy.uix.screenmanager import  NoTransition, ScreenManager , Screen
from login import Stater , SignScreen ,ForPassScreen , ChangePassScreen 
from kivy.clock import Clock
from home import Home
from search import Listi , Book , Search
from wishlist import Wishlist
from profile import Profile
from client import RequestUtil
req_util=RequestUtil()
pre_slide=0
class NavigationScreen(Screen):
    pass
class SUBApp(MDApp):
    my_otp=NumericProperty()
    def build(self):
        Builder.load_file('home.kv')
        Builder.load_file('login.kv')
        Builder.load_file('search.kv')
        Builder.load_file('wishlist.kv')
        Builder.load_file('profile.kv')
        self.manager=ScreenManager(transition=NoTransition())
        self.starting_page=Stater(name='stater')
        self.manager.add_widget(self.starting_page)
        self.manager.add_widget(SignScreen(name='signin'))
        self.manager.add_widget(ForPassScreen(name='forpass'))
        self.manager.add_widget(ChangePassScreen(name='change_passo'))
        self.layout=NavigationScreen(name='nav')
        self.manager.add_widget(Search(name='search'))
        self.manager.add_widget(self.layout)
        return self.manager
    def on_start(self):
        Clock.schedule_interval(self.show, .3)
        return super().on_start()
    def show(self,dt):
        global pre_slide
        cur=self.starting_page.sp.index
        if self.manager.current_screen==self.starting_page:
            return False
        if pre_slide!=cur:
            print(cur)
            self.starting_page.ind.change(cur)
            pre_slide=cur
    def set_list_books(self, text="", search=False):
        def add_icon_item(quantity,author,title,edition,pub,year):
            vo=Listi()
            vo.add(quantity,author,title,edition,pub,year)
            self.layout.ids.mehtha.ids.lis.add_widget(vo)
            
        def searchme(search):
            if search:
                me=req_util.make_get_request(ENDPOINT_ROUTE="search",token=text)
                self.layout.ids.mehtha.ids.lis.clear_widgets()
                for row in me:
                    quantity,author,title,edition,pub,year=row
                    book=Book(quantity,author,title,edition,pub,year)
                    add_icon_item(book.quantity,book.author,book.title,book.edition,book.pub,book.year)
                return False
            else:
                me=req_util.make_get_request(ENDPOINT_ROUTE="",token=text)
                self.layout.ids.mehtha.ids.lis.clear_widgets()
                for row in me:
                    quantity,author,title,edition,pub,year=row
                    book=Book(quantity,author,title,edition,pub,year)
                    add_icon_item(book.quantity,book.author,book.title,book.edition,book.pub,book.year)
                return False
        Clock.schedule_interval(searchme, .4)
if __name__ == "__main__":
    SUBApp().run()