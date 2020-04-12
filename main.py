from extrapolation import plot_values

try:
    import kivy
except ImportError:
    raise ImportError("You don't have Kivy installed!")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.factory import Factory
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.lang import Builder

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
        self.polynomial_degree = 0

    def poly_degree(self, widget, message, *args):
        widget.text = message[2]

    def set_selected_file(self, *args):
        try:
            print(args[1][0])
            self.source_file_path = args[1][0]
        except IndexError:
            print("Index error??")
            pass

    def launch_plotting(self):
        file_path = 'C:/Users/Dan/Dropbox/Savings.xlsx'
        plot_values(file_path, extrapolated_days=365*4)
        # try:
        #     if self.source_file_path is not "":
        #         plot_values(self.source_file_path, extrapolated_days=1000)
        #     else:
        #         MessagePopup.create_popup_with_text("Please select a source file before running")
        # except Exception as e:
        #     MessagePopup.create_popup_with_text("Error: " + str(e))


class RootWidget(Widget):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)


class DemoApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    DemoApp().run()