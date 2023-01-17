from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
Window.size = (350, 580)


class MenuScreen(Screen):
    pass

class LoginScreen(Screen):
    pass

class SignupScreen(Screen):
    pass


sn= ScreenManager()
sn.add_widget(MenuScreen(name="menu"))
sn.add_widget(SignupScreen(name="signup"))
sn.add_widget(LoginScreen(name="login"))


class TestApp(MDApp):
    def build(self):
        Builder.load_file("test.kv")


TestApp().run()
