from kivy.uix.boxlayout import BoxLayout
from header import Header
from categories_section import CategoriesSection
from navigation_bar import NavigationBar
from kivy.uix.label import Label


class LandingPage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = 'vertical'

        self.add_widget(Header())
        self.add_widget(CategoriesSection())
        self.add_widget(Label(text="Hello World!"))
        self.add_widget(NavigationBar())

