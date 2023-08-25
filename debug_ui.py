from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from subcategories import SubcategoriesScreen

# Load the kv file and build the widget
Builder.load_file('subcategories.kv')
screen = SubcategoriesScreen(category_id='dummy_id', category_name='dummy_name')

# Print the UI tree
runTouchApp(screen)
