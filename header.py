from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.label import Label


class Header(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Set the orientation of the Header to vertical
        self.orientation = 'vertical'

        # Apply the pink background
        with self.canvas.before:
            Color(1, 0.5, 0.5, 1)  # Pink color (RGBA)
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect, pos=self._update_rect)

        # Add a Label with the "What are you looking for?" text
        label = Label(text="What are you looking for?", size_hint_y=None, height=30)
        self.add_widget(label)

        # Create a horizontal layout for search bar and button
        search_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)

        # Add a TextInput for the search bar
        search_box = TextInput(hint_text="Search", size_hint_x=0.5)
        search_layout.add_widget(search_box)

        # Add a Button for the search action
        search_button = Button(text="Search", size_hint_x=0.3)
        search_layout.add_widget(search_button)

        self.add_widget(search_layout)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
