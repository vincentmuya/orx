from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from landing_page import LandingPage
from subcategories import SubcategoriesScreen
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

    def on_category_button(self, instance, category_name):
        print(f"Selected category: {category_name}")
        app = App.get_running_app()

        # Get the parent_id based on the category_name
        url = f'http://localhost:8000/api/category-id/{category_name}/'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            parent_id = data.get('category_id')
            if parent_id is not None:
                # Create an instance of SubcategoriesScreen with the correct arguments
                self.subcategories_screen = SubcategoriesScreen(parent_id=parent_id, category_name=category_name)

                # Remove the previous subcategories screen if it exists
                if 'subcategories_screen' in self.screen_manager.screen_names:
                    self.screen_manager.remove_widget(self.screen_manager.get_screen('subcategories_screen'))

                # Create a new screen and add the SubcategoriesScreen instance
                subcategories_screen_screen = Screen(name='subcategories_screen')
                subcategories_screen_screen.add_widget(subcategories_screen)
                self.screen_manager.add_widget(subcategories_screen_screen)

                self.screen_manager.current = 'subcategories_screen'  # Switch to the new screen
            else:
                print("Category ID not found")
        else:
            print("Failed to get category ID")


if __name__ == '__main__':
    MyApp().run()
