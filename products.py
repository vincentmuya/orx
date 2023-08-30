from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen


class ProductsScreen(Screen):
    def load_products(self, products_data):
        print("Loading products...")
        print("self.ids:", self.ids)
        products_layout = self.ids.products_layout
        products_layout.clear_widgets()

        for product in products_data:
            product_label = Label(text=f"Title: {product['title']}\nPrice: {product['price']}")
            products_layout.add_widget(product_label)
