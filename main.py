from kivy.app import App
from landing_page import LandingPage


class MyApp(App):
    def build(self):
        return LandingPage()


if __name__ == '__main__':
    MyApp().run()
