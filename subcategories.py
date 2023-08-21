from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import requests


class SubcategoriesScreen(BoxLayout):
    def __init__(self, parent_id, **kwargs):
        super().__init__(**kwargs)

        self.parent_id = parent_id  # Store the parent ID

        self.orientation = 'vertical'
        self.load_subcategories(parent_id)

    def load_subcategories(self, parent_id):
        # Make API request to Django backend to get subcategories based on parent_id
        response = requests.get(f'http://localhost:8000/api/category/{parent_id}/subcategories/')

        if response.status_code == 404:
            print("Subcategories API endpoint not found")
        else:
            try:
                data = response.json()
                # Create Kivy buttons to display subcategories
                for subcategory in data:
                    subcategory_button = Button(text=subcategory['name'])
                    self.add_widget(subcategory_button)
                    subcategory_button.bind(on_release=self.on_subcategory_button)
            except requests.exceptions.JSONDecodeError as e:
                print("Error decoding JSON response:", e)
                print("Response content:", response.content)

    def on_subcategory_button(self, instance):
        subcategory_name = instance.text
        print(f"Selected subcategory: {subcategory_name}")
        # You can implement further navigation or actions here
