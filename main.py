from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from landing_page import LandingPage
from subcategories import SubcategoriesScreen


class MyApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        # Create and add the landing page screen
        landing_page_screen = Screen(name='landing_page')
        landing_page = LandingPage()
        landing_page_screen.add_widget(landing_page)
        self.screen_manager.add_widget(landing_page_screen)

        # Create and add the subcategories screen
        subcategories_screen = Screen(name='subcategories_screen')
        subcategories = SubcategoriesScreen(parent_id='')
        subcategories_screen.add_widget(subcategories)
        self.screen_manager.add_widget(subcategories_screen)

        return self.screen_manager


if __name__ == '__main__':
    MyApp().run()
