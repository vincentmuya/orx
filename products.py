from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
import requests
from kivy.app import App
from kivy.uix.screenmanager import SlideTransition


Builder.load_file('products.kv')


class ProductCard(BoxLayout):
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


class ProductsScreen(Screen):
    def load_products(self, products_data):
        print("Loading products...")
        print("self.ids:", self.ids)
        print("Products Data:", products_data)
        products_layout = self.ids.products_layout
        products_layout.clear_widgets()

        for product in products_data:
            product_card = ProductCard(title=product['title'], price=str(product['price']),
                                       image_source=product['image'], product_id=str(product['id']), slug=product['slug'])
            products_layout.add_widget(product_card)
