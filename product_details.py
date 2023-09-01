from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.lang import Builder

Builder.load_file('product_details.kv')


class ProductDetailsScreen(Screen):
    def load_details(self, product_details):
        print("Loading product_details...")
        print("self.ids:", self.ids)
        print("Products Details:", product_details)


