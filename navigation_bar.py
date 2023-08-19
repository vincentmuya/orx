from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle


class NavigationBar(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Set the orientation of the NavigationBar to horizontal
        self.orientation = 'horizontal'

        # Set the height of the NavigationBar
        self.size_hint_y = None
        self.height = 50  # Adjust the height as needed

        # Apply the grey background
        with self.canvas.before:
            Color(0.5, 0.5, 0.5, 1)  # Grey color (RGBA)
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect, pos=self._update_rect)

        # Create a container layout for evenly spaced items
        container = BoxLayout(orientation='horizontal', spacing=10)

        # Add Home Button
        home_button = Button(text="Home", size_hint=(None, None), size=(100, 50))
        container.add_widget(home_button)

        # Add Profile Button
        profile_button = Button(text="Profile", size_hint=(None, None), size=(100, 50))
        container.add_widget(profile_button)

        # Add Add Product Button
        add_product_button = Button(text="Add Product", size_hint=(None, None), size=(150, 50))
        container.add_widget(add_product_button)

        # Add Contact Button
        contact_button = Button(text="Contact", size_hint=(None, None), size=(150, 50))
        container.add_widget(contact_button)

        self.add_widget(container)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
