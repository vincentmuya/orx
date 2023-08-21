from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from functools import partial
import requests


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
            ('image1.png', 'Car and Vehicles'),
            ('image2.png', 'Electronics'),
            ('image3.png', 'Fashion'),
            ('image4.png', 'Food and Agriculture'),
            ('image5.png', 'Health And Beauty'),
            ('image6.png', 'Hobby, Sports And Kids'),
            ('image7.png', 'Home, Furniture And Appliances'),
            ('image8.png', 'Industry Machinery and Tools'),
            ('image9.png', 'Jobs'),
            # Add more categories as needed
        ]

        for image_source, caption in categories:
            category_layout = BoxLayout(orientation='vertical', size_hint=(None, None))

            # Add an Image for the category
            category_image = Image(source=image_source, size_hint_y=None, height=40)
            category_layout.add_widget(category_image)

            # Add a Label for the caption
            category_caption = Label(text=caption, size_hint_y=None, height=30)
            category_layout.add_widget(category_caption)

            # Create a button for the category
            category_button = Button(text=caption)
            category_layout.add_widget(category_button)

            # Bind the button's on_release event to a method that handles it
            category_button.bind(on_release=partial(self.on_category_button, category_name=caption))

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
    def on_category_button(self, instance, category_name):
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
                # Update the category ID in the subcategories screen
                app.subcategories_screen.category_id = category_id

                # Switch to the subcategories screen
                app.root.current = 'subcategories_screen'
            else:
                print("Category ID not found")
        else:
            print("Failed to get category ID")
