from kivy.uix.screenmanager import Screen
import requests


class AddProductsScreen(Screen):
    def add_product(self):
        # Define the form data as a dictionary
        form_data = {
            'field1': 'value1',
            'field2': 'value2',
            # Add more fields as needed
        }
        # Make a POST request to the API endpoint
        api_url = 'http://localhost:8000/api/new-product/'
        response = requests.post(api_url, json=form_data)

        # Handle the response
        if response.status_code == 201:  # 201 indicates a successful creation
            print("Product created successfully")
        elif response.status_code == 400:
            print("Form submission failed. Validation error.")
        else:
            print("Form submission failed. Unknown error.")
        pass