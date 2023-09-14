from kivy.uix.screenmanager import Screen
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.uix.image import AsyncImage

Builder.load_file('products.kv')


class ItemsCard(BoxLayout):
    title = StringProperty()
    price = StringProperty()
    image_source = StringProperty()
    slug = StringProperty()
    product_id = StringProperty()


class ItemsScreen(Screen):
    def items(self):
        response = requests.get(f'http://localhost:8000/api/product/')
        print("Items", response)

        if response.status_code == 200:
            items = response.json()
            print("Items", items)
            self.load_items(items)

            # Access the ScreenManager through the App instance
            app = App.get_running_app()
            items_screen = app.root.get_screen('items')

            # Load the items into the ItemsScreen instance
            items_screen.load_items(items)

    def load_items(self, items):
        items_layout = self.ids.items_layout
        items_layout.clear_widgets()
        for item in items:

            items_card = ItemsCard(title=item['title'], price=str(item['price']), image_source=item['image'], product_id=str(item['id']), slug=item['slug'])
            items_layout.add_widget(items_card)
            pass  # Implement this method to update your UI
