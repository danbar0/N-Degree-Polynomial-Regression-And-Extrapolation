import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.properties import StringProperty
from kivy.lang import Builder
from extrapolation import plot_values
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.config import Config

Builder.load_file('kivySource.kv')
DEBUG = False

class MessagePopup(Popup):
    message_text = StringProperty()

    def __init__(self, message="null", **kwargs):
        super(MessagePopup, self).__init__(**kwargs)
        self.message_text = message
        self.popup_open = False

    def dismiss_event(self):
        self.dismiss()
        self.popup_open = False

    def open_with_text(self, message):
        if self.popup_open is True:
            return

        self.message_text = message
        self.open()
        self.popup_open = True


class SelectionMenu(FloatLayout):
    def __init__(self, **kwargs):
        super(SelectionMenu, self).__init__(**kwargs)
        self.source_file_path = ""
        self.sheet_name = ""
        self.days_to_extrapolate = 1
        self.target_net_worth = 0
        self.polynomial_degree = 2
        self.popup = MessagePopup("null")

    def poly_degree(self, widget, message, *args):
        widget.text = message[2]

    def set_sheet_name(self, name=""):
        print(name)
        self.sheet_name = name

    def set_selected_file(self, *args):
        try:
            print(args[1][0])
            self.source_file_path = args[1][0]
        except IndexError:
            print("Index error??")
            pass

    def launch_plotting(self):
        try:
            if self.source_file_path is not "":
                print(self.sheet_name)
                plot_values(self.source_file_path, self.sheet_name, degree=self.polynomial_degree, extrapolated_days=self.days_to_extrapolate)
            else:
                self.popup.open_with_text("Please select a source file before running")

        except Exception as e:
            self.popup.open_with_text("Error: " + str(e))

    def set_degree(self, degree='2'):
        if degree == '':
            return

        if 1 <= int(degree) < 100:
            print(degree)
            self.polynomial_degree = int(degree)
        else:
            self.popup.open_with_text("Degree is limited to a value of 100 and cannot be negative")

    def set_days_to_extrapolate(self, days='10'):
        if days == '':
            return

        if 1 <= int(days) < 36500:
            self.days_to_extrapolate = int(days)
        else:
            self.popup.open_with_text("Future date must be less than 100 years from now and greater than 0")

    def set_target_net_worth(self, target):
        self.target_net_worth = target


class RootWidget(Widget):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)


class DemoApp(App):
    def build(self):
        Window.size = (1000, 800)
        self.title = "Regression And Extrapolation"

        return RootWidget()


if __name__ == '__main__':
    Config.set('graphics', 'resizable', False)

    DemoApp().run()