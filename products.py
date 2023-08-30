from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file('products.kv')


class ProductsScreen(Screen):
    def load_products(self, products_data):
        print("Loading products...")
        print("self.ids:", self.ids)
        print("Products Data:", products_data)
        products_layout = self.ids.products_layout
        products_layout.clear_widgets()

        for product in products_data:
            product_label = Label(text=f"Title: {product['title']}\nPrice: {product['price']}")
            products_layout.add_widget(product_label)
