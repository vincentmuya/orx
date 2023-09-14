from kivy.uix.screenmanager import Screen
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.uix.image import AsyncImage

Builder.load_file('items.kv')


class ItemsCard(BoxLayout):
    title = StringProperty()
    price = StringProperty()
    image_source = StringProperty()
    slug = StringProperty()
    product_id = StringProperty()


class ItemsScreen(Screen):
    def __init__(self, **kwargs):
        super(ItemsScreen, self).__init__(**kwargs)
        self.load_items()

    def load_items(self):
        response = requests.get(f'http://localhost:8000/api/product/')
        if response.status_code == 200:
            items = response.json()
            print("items:", items)

            self.clear_items()  # Clear any existing items before loading new ones
            for item in items:
                full_image_url = f"http://localhost:8000{item['image']}"
                items_card = ItemsCard(
                    title=item['title'],
                    price=str(item['price']),
                    image_source=full_image_url,
                    product_id=str(item['id']),
                    slug=item['slug']
                )
                self.add_item(items_card)

    def clear_items(self):
        # Clear the items_layout before adding new items
        items_layout = self.ids.items_layout
        items_layout.clear_widgets()

    def add_item(self, item):
        # Add a new item to the items_layout
        items_layout = self.ids.items_layout
        items_layout.add_widget(item)
