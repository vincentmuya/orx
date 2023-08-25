from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import requests
from kivy.clock import Clock


Builder.load_file('subcategories.kv')


class SubcategoriesScreen(BoxLayout):
    def __init__(self, category_id, category_name, **kwargs):
        super().__init__(**kwargs)
        print("Loading SubcategoriesScreen from KV")

        self.category_name = category_name  # Store the clicked category name
        self.category_id = category_id  # Initialize the category_id attribute

        self.orientation = 'vertical'
        self.load_subcategories()

    def load_subcategories(self):
        # Make API request to Django backend to get parent_id based on category_name
        response = requests.get(f'http://localhost:8000/api/category-id/{self.category_name}/')
        print("API Response Content Category ID:", response.content)

        if response.status_code == 200:
            data = response.json()
            parent_id = data.get('category_id')

            if parent_id is not None:
                # Make another API request to get subcategories based on parent_id
                subcategories_response = requests.get(f'http://localhost:8000/api/category/{parent_id}/subcategories/')
                if subcategories_response.status_code == 200:
                    subcategories_data = subcategories_response.json()
                    print("Subcategories & Parent ", subcategories_response.content)

                    self.ids.grid_layout.clear_widgets()

                    # Create Kivy buttons to display subcategories
                    for subcategory in subcategories_data:
                        subcategory_name = subcategory['name']
                        print(f"Creating subcategory button: {subcategory_name}")
                        subcategory_button = Button(text=subcategory_name)
                        self.ids.grid_layout.add_widget(subcategory_button)
                        subcategory_button.bind(on_release=self.on_subcategory_button)
                    self.ids.grid_layout.do_layout()
                else:
                    print("Subcategories API endpoint not found")
            else:
                print("Parent category not found")
        else:
            print("Failed to get parent_id")

    def on_subcategory_button(self, instance):
        print("Button clicked:", instance.text)
        subcategory_name = instance.text
        print(f"Selected subcategory: {subcategory_name}")
        # You can implement further navigation or actions here
