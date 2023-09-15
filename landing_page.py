from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from header import Header
from body_section import BodySection
from navigation_bar import NavigationBar
from items import ItemsScreen


class LandingPage(ScrollView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.scroll_type = ['bars']
        self.bar_width = 10
        self.do_scroll_x = False  # Disable horizontal scrolling
        self.do_scroll_y = True   # Enable vertical scrolling

        # Create a vertical BoxLayout to stack the screens
        self.layout = BoxLayout(orientation='vertical', spacing=10, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))

        # Create and wrap screens with specific heights
        header = self.wrap_screen(Header(), height=200)
        body = self.wrap_screen(BodySection(), height=300)
        items_screen = self.wrap_screen(ItemsScreen(), height=600)
        nav_bar = self.wrap_screen(NavigationBar(), height=100)

        # Add the wrapped screens to the layout
        self.layout.add_widget(header)
        self.layout.add_widget(body)
        self.layout.add_widget(items_screen)
        self.layout.add_widget(nav_bar)

        # Set the layout as the content of the ScrollView
        self.add_widget(self.layout)

    def wrap_screen(self, screen, height):
        """
        Wrap a screen in a layout with a specific height.
        """
        layout = BoxLayout(orientation='vertical', size_hint_y=None, height=height)
        layout.add_widget(screen)
        return layout
