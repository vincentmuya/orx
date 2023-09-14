from kivy.uix.boxlayout import BoxLayout
from header import Header
from body_section import BodySection
from navigation_bar import NavigationBar
from kivy.uix.label import Label
from items import ItemsScreen


class LandingPage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = 'vertical'

        self.add_widget(Header())
        self.add_widget(BoxLayout(size_hint_y=None, height=0))

        self.add_widget(BodySection())
        self.add_widget(ItemsScreen())
        self.add_widget(NavigationBar())

