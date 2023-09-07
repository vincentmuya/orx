from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.lang import Builder
from navigation_bar import NavigationBar

Builder.load_file('product_details.kv')


class ProductDetailsScreen(Screen):
    title = StringProperty()
    price = StringProperty()
    description = StringProperty()
    image_source = StringProperty()

    def load_details(self, product_details):
        print("Loading product_details...")
        print("self.ids:", self.ids)
        print("Products Details:", product_details)
        product_details_layout = self.ids.product_details_layout
        product_details_layout.clear_widgets()

        self.title = product_details['title']
        self.price = str(product_details['price'])
        self.description = product_details['description']
        self.image_source = f"http://localhost:8000{product_details['image']}"

        title_label = self.ids.title_label
        title_label.text = self.title
        price_label = self.ids.price_label
        price_label.text = self.price
        description_label = self.ids.description_label
        description_label.text = self.description

        self.add_widget(NavigationBar())
