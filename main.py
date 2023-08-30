from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from landing_page import LandingPage
from subcategories import SubcategoriesScreen
from products import ProductsScreen


class MyApp(App):
    def build(self):
        self.subcategories_screen = None  # Initialize the subcategories_screen attribute
        self.screen_manager = ScreenManager()

        # Create and add the landing page screen
        landing_page_screen = Screen(name='landing_page')
        landing_page = LandingPage()
        landing_page_screen.add_widget(landing_page)
        self.screen_manager.add_widget(landing_page_screen)

        # Read category_id and category_name from the file
        with open('category_info.txt', 'r') as f:
            lines = f.readlines()
            category_id = int(lines[0].strip())
            category_name = lines[1].strip()

        # Create a Screen to encapsulate the SubcategoriesScreen
        subcategories_screen = Screen(name='subcategories_screen')
        subcategories_content = SubcategoriesScreen(category_id, category_name)
        subcategories_screen.add_widget(subcategories_content)
        self.screen_manager.add_widget(subcategories_screen)

        # Create the ProductsScreen instance and add it to the ScreenManager
        products_screen = ProductsScreen(name='products')
        self.screen_manager.add_widget(products_screen)

        return self.screen_manager


if __name__ == '__main__':
    MyApp().run()
