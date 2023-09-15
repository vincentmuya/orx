from kivy.uix.screenmanager import Screen
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import SlideTransition
from kivy.uix.image import AsyncImage

Builder.load_file('items.kv')


class ItemsCard(BoxLayout):
    title = StringProperty()
    price = StringProperty()
    image_source = StringProperty()
    slug = StringProperty()
    product_id = StringProperty()

    def view_product(self):
        # Access the product ID associated with this card
        product_id = self.product_id

        # Fetch the product details from the API using requests
        api_url = f"http://localhost:8000/api/product/{product_id}/{self.slug}/"
        response = requests.get(api_url)
        print("API Product Details:", response.content)
        if response.status_code == 200:
            product_details = response.json()
            print("Product Details:", product_details)
            # Now you have the product details, you can pass them to the next screen
            # Access the ScreenManager and switch to the next screen
            app = App.get_running_app()
            product_details_screen = app.root.get_screen('product_details')

            # Load the products into the ProductsScreen instance
            product_details_screen.load_details(product_details)

            # Transition to the ProductsScreen
            app.root.transition = SlideTransition(direction='left')
            app.root.current = 'product_details'
        else:
            print("Failed to fetch product details.")


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
