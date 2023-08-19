from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label


class CategoriesSection(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Set the orientation of the CategoriesSection to horizontal
        self.orientation = 'horizontal'

        # Set padding between the CategoriesSection and the Header
        self.padding = [0, 20, 0, 0]  # Top, Right, Bottom, Left

        # Set padding between each category
        self.spacing = 10

        # Example category data: list of tuples (image source, caption)
        categories = [
            ('image1.png', 'Category 1'),
            ('image2.png', 'Category 2'),
            ('image3.png', 'Category 3'),
            ('image4.png', 'Category 4'),
            # Add more categories as needed
        ]

        for image_source, caption in categories:
            category_layout = BoxLayout(orientation='vertical', size_hint_x=None, width=150)

            # Add an Image for the category
            category_image = Image(source=image_source, size_hint_y=None, height=100)
            category_layout.add_widget(category_image)

            # Add a Label for the caption
            category_caption = Label(text=caption)
            category_layout.add_widget(category_caption)

            self.add_widget(category_layout)
