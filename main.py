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

        # Create and add the subcategories screen (Note: Do not create an instance here)
        subcategories_screen = Screen(name='subcategories_screen')
        self.screen_manager.add_widget(subcategories_screen)  # Add the screen without an instance

        return self.screen_manager

    def on_category_button(self, instance, category_name):
        print(f"Selected category: {category_name}")
        app = App.get_running_app()

        # Set the category name in the subcategories screen
        app.subcategories_screen.category_name = category_name

        app.root.current = 'subcategories_screen'


if __name__ == '__main__':
    MyApp().run()
