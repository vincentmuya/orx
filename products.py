from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

Builder.load_file('products.kv')


class ProductCard(BoxLayout):
    title = StringProperty()
    price = StringProperty()
    image_source = StringProperty()

    def view_product(self):
        # Define the behavior when the button is pressed
        pass


class ProductsScreen(Screen):
    def load_products(self, products_data):
        print("Loading products...")
        print("self.ids:", self.ids)
        print("Products Data:", products_data)
        products_layout = self.ids.products_layout
        products_layout.clear_widgets()

        for product in products_data:
            product_card = ProductCard(title=product['title'], price=str(product['price']),
                                       image_source=product['image'])
            products_layout.add_widget(product_card)
