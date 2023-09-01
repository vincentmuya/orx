from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.lang import Builder

Builder.load_file('product_details.kv')


class ProductDetailsScreen(Screen):
    title = StringProperty()
    price = StringProperty()

    def load_details(self, product_details):
        print("Loading product_details...")
        print("self.ids:", self.ids)
        print("Products Details:", product_details)
        product_details_layout = self.ids.product_details_layout
        product_details_layout.clear_widgets()

        self.title = product_details['title']
        self.price = str(product_details['price'])
        title_label = self.ids.title_label
        title_label.text = self.title
        price_label = self.ids.price_label
        price_label.text = self.price
