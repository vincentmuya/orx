from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from landing_page import LandingPage
import requests


class MyApp(App):
    def build(self):
        self.subcategories_screen = None  # Initialize the subcategories_screen attribute
        self.screen_manager = ScreenManager()

        # Create and add the landing page screen
        landing_page_screen = Screen(name='landing_page')
        landing_page = LandingPage()
        landing_page_screen.add_widget(landing_page)
        self.screen_manager.add_widget(landing_page_screen)

        return self.screen_manager


if __name__ == '__main__':
    MyApp().run()
