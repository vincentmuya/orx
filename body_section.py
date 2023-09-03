from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from functools import partial
import requests
from subcategories import SubcategoriesScreen


class BodySection(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Set the orientation of the BodySection to vertical
        self.orientation = 'vertical'

        # Create a GridLayout to arrange categories in rows
        categories_grid = GridLayout(cols=4, spacing=50, size_hint_y=None)
        categories_grid.bind(minimum_height=categories_grid.setter('height'))

        # Example category data
        categories = [
            ('images/icons/cars.png', 'Car and Vehicles'),
            ('images/icons/electronics.png', 'Electronics'),
            ('images/icons/fashion.png', 'Fashion'),
            ('images/icons/food.png', 'Food and Agriculture'),
            ('images/icons/hair.png', 'Health And Beauty'),
            ('images/icons/hobbies.png', 'Hobby, Sports And Kids'),
            ('images/icons/furniture.png', 'Home, Furniture And Appliances'),
            ('images/icons/industry.png', 'Industry Machinery and Tools'),
            ('images/icons/jobs.png', 'Jobs'),
            # Add more categories as needed
        ]

        for image_source, caption in categories:
            category_layout = BoxLayout(orientation='vertical', size_hint=(None, None))

            # Add an Image for the category
            category_image = Image(source=image_source, size_hint_y=None, height=60)
            category_layout.add_widget(category_image)

            # Add a Label for the caption
            category_caption = Label(text=caption, size_hint_y=None, height=20)
            category_layout.add_widget(category_caption)

            # Bind the category_caption's on_touch_down event to a method that handles it
            category_caption.bind(on_touch_down=partial(self.on_category_caption, category_name=caption))

            categories_grid.add_widget(category_layout)

            # Check if the current row in the GridLayout is full
            if len(categories_grid.children) % 4 == 0:
                self.add_widget(categories_grid)
                categories_grid = GridLayout(cols=4, spacing=50, size_hint_y=None)
                categories_grid.bind(minimum_height=categories_grid.setter('height'))

        # If there are remaining items that didn't fill the last row completely
        if categories_grid.children:
            self.add_widget(categories_grid)

    # Update your on_category_button method
    def on_category_caption(self, instance, touch, category_name):
        if touch.is_mouse_scrolling:
            return  # Ignore mouse scroll events

        if instance.collide_point(*touch.pos):
            category_name = instance.text
            print(f"Selected category: {category_name}")
            app = App.get_running_app()

            # Make API request to get category ID based on category name
            url = f'http://localhost:8000/api/category-id/{category_name}/'
            response = requests.get(url)
            print("API Response Content:", response.content)

            if response.status_code == 200:
                data = response.json()
                category_id = data.get('category_id')
                if category_id is not None:
                    # Create an instance of SubcategoriesScreen with the correct arguments
                    subcategories_screen = SubcategoriesScreen(category_id=category_id, category_name=category_name)

                    # Set the subcategories screen in the app
                    app.subcategories_screen = subcategories_screen

                    # Switch to the subcategories screen
                    app.root.current = 'subcategories_screen'
                else:
                    print("Category ID not found")
            else:
                print("Failed to get category ID")