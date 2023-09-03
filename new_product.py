from kivy.uix.screenmanager import Screen
import requests
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('new_product.kv')


class AddProductsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.form_fields = {}  # Store form fields in a dictionary

        # Create and add form fields dynamically based on API data
        self.load_form_fields_from_api()

    def load_form_fields_from_api(self):
        # Make a GET request to the API to fetch form field data
        api_url = 'http://localhost:8000/api/new-product/'  # Replace with the actual API endpoint
        response = requests.get(api_url)

        if response.status_code == 200:
            api_data = response.json()

            # Create form fields based on the API data
            for field_name, field_value in api_data.items():
                text_input = TextInput(hint_text=field_name)
                self.form_fields[field_name] = text_input
                self.add_widget(text_input)

            # Add a Submit button
            submit_button = Button(text="Submit", on_release=self.submit_form)
            self.add_widget(submit_button)

    def submit_form(self, instance):
        # Collect form data from the form fields
        form_data = {}
        for field_name, text_input in self.form_fields.items():
            form_data[field_name] = text_input.text

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