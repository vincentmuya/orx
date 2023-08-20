from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label


class CategoriesSection(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Set the orientation of the CategoriesSection to vertical
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

            categories_grid.add_widget(category_layout)

            # Check if the current row in the GridLayout is full
            if len(categories_grid.children) % 4 == 0:
                self.add_widget(categories_grid)
                categories_grid = GridLayout(cols=4, spacing=50, size_hint_y=None)
                categories_grid.bind(minimum_height=categories_grid.setter('height'))

        # If there are remaining items that didn't fill the last row completely
        if categories_grid.children:
            self.add_widget(categories_grid)
