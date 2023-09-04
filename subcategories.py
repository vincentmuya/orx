from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import requests
from kivy.app import App
from kivy.uix.screenmanager import SlideTransition
from navigation_bar import NavigationBar

Builder.load_file('subcategories.kv')


class SubcategoriesScreen(BoxLayout):
    def __init__(self, category_id, category_name, **kwargs):
        super().__init__(**kwargs)

        self.category_name = category_name  # Store the clicked category name
        self.category_id = category_id  # Initialize the category_id attribute

        self.orientation = 'vertical'
        self.load_subcategories()
        self.add_widget(NavigationBar())


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

                    # Reference the GridLayout defined in the subcategories.kv file
                    grid_layout = self.ids.grid_layout
                    print("self.ids:", self.ids)
                    grid_layout.clear_widgets()

                    # Clear any existing widgets in the GridLayout
                    grid_layout.clear_widgets()
                    # Create Kivy buttons to display subcategories
                    for subcategory in subcategories_data:
                        subcategory_button = Button(text=subcategory['name'])
                        self.add_widget(subcategory_button)
                        subcategory_button.bind(on_release=self.on_subcategory_button)
                    # Write the category_id and category_name to a file
                    with open('category_info.txt', 'w') as f:
                        f.write(f"{parent_id}\n{self.category_name}")
                else:
                    print("Subcategories API endpoint not found")
            else:
                print("Parent category not found")
        else:
            print("Failed to get parent_id")

    def on_subcategory_button(self, instance):
        subcategory_name = instance.text
        print(f"Selected subcategory: {subcategory_name}")

        # Make an API request to get the category_id based on the subcategory_name
        category_id_response = requests.get(f'http://localhost:8000/api/category-id/{subcategory_name}/')
        print("Category ID Response Response:", category_id_response.content)

        if category_id_response.status_code == 200:
            category_id_data = category_id_response.json()
            category_id = category_id_data.get('category_id')
            print("API Category ID Response:", category_id)

            if category_id is not None:
                # Make an API request to get products based on the category_id
                products_response = requests.get(f'http://localhost:8000/api/product/?category_id={category_id}')
                print("API Product Response:", products_response.content)
                if products_response.status_code == 200:
                    products_data = products_response.json()
                    print("Products:", products_data)

                    # Access the ScreenManager through the App instance
                    app = App.get_running_app()
                    products_screen = app.root.get_screen('products')

                    # Load the products into the ProductsScreen instance
                    products_screen.load_products(products_data)

                    # Transition to the ProductsScreen
                    app.root.transition = SlideTransition(direction='left')
                    app.root.current = 'products'

                else:
                    print("Failed to get products for the selected category_id")
            else:
                print("Category ID not found in the response")
        else:
            print("Failed to get category_id for the selected subcategory")
