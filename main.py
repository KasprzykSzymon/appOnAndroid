from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget

class WidgetsExample(GridLayout):
    count = 1
    my_text = StringProperty("1")
    def on_button_click(self):
        print("You press button")
        self.my_text = str(self.count)
        self.count +=1
class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class MainWidget(Widget):
    pass
class AndroidAPP(App):
    pass
    # def build(self):
    #     return Button(text="Hello World")

AndroidAPP().run()