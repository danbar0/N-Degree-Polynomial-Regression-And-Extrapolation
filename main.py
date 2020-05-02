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


Builder.load_file('kivySource.kv')


class MessagePopup(Popup):
    message_text = StringProperty()

    def __init__(self, message="null", **kwargs):
        super(MessagePopup, self).__init__(**kwargs)
        self.message_text = message

    @staticmethod
    def create_popup_with_text(message):
        popup = MessagePopup(message)
        popup.open()


class SelectionMenu(FloatLayout):
    def __init__(self, **kwargs):
        super(SelectionMenu, self).__init__(**kwargs)
        self.source_file_path = ""
        self.sheet_name = ""
        self.days_to_extrapolate = 1
        self.target_net_worth = 0
        self.polynomial_degree = 0

    def poly_degree(self, widget, message, *args):
        widget.text = message[2]

    def set_sheet_name(self, name=""):
        self.sheet_name = name

    def set_selected_file(self, *args):
        try:
            print(args[1][0])
            self.source_file_path = args[1][0]
        except IndexError:
            print("Index error??")
            pass

    def launch_plotting(self):
        self.source_file_path = 'C:/Users/Dan/Dropbox/Savings.xlsx'

        try:
            if self.source_file_path is not "":
                plot_values(self.source_file_path, self.sheet_name, extrapolated_days=self.days_to_extrapolate)
            else:
                MessagePopup.create_popup_with_text("Please select a source file before running")

        except Exception as e:
            MessagePopup.create_popup_with_text("Error: " + str(e))

    def set_days_to_extrapolate(self, days='10'):
        if days == '':
            return

        if int(days) < 36500:
            self.days_to_extrapolate = int(days)
        else:
            MessagePopup.create_popup_with_text("Future date must be less than 100 years from now")

    def set_target_net_worth(self, target):
        self.target_net_worth = target


class RootWidget(Widget):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)


class DemoApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    DemoApp().run()