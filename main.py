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
from kivy.lang import Builder
from kivy.graphics import *

Builder.load_string('''
#:kivy 1.10.0

<StartButton>:
    FloatLayout:
        Button:
            pos_hint:   {'center_x': 0.3, 'center_y': 0.25}
            size_hint:  (0.1, 0.1)
            text:       '-'
            on_press: 

<SelectionMenu>:
    FloatLayout:
        # Background
        Image:
            source: 'background.png'
            size: self.texture_size
            
        # User Directions
        Label:
            text: "Set parameters and select a source file"
            pos_hint: {'center_x': 0.2, 'center_y': 0.95}
            
        # Launch Button
        Button:
            pos: (20, 20)
            #pos_hint: {'x':.2, 'y':.2}
            size_hint:  .47, .1
            text:       'Run'
            on_release: root.launch_plotting()
            
        Button:
            pos_hint:   {'center_x': 0.25, 'center_y': 0.25}
            size_hint:  .05, .05
            text:       '+'
            
        Button:
            pos_hint:   {'center_x': 0.3, 'center_y': 0.25}
            size_hint:  .05, .05
            text:       '-'
            
        Label:
            pos_hint:   {'_x': 0.4, 'center_y': 0.25}
            size_hint:  .05, .05
            text:       'test'
            
        FileChooserListView:
            size_hint:      0.5, 1
            pos_hint:       {'center_x': 0.75, 'center_y': 0.5}
            on_selection:   root.selected_file(*args)

            
<ExceptionPopup>:
    Label:
        text: "test"
    Button:
        text: "close"
        on_release: root.close_popup(*args)
                
<RootWidget>:
    FloatLayout:
        size: root.size
        pos: root.pos
        
        SelectionMenu:
            
''')


class ExceptionPopup(Popup):

    def close_popup(self):
        pass


class SelectionMenu(FloatLayout):
    def __init__(self, **kwargs):
        super(SelectionMenu, self).__init__(**kwargs)
        self.source_file_path = ""
        self.polynomial_degree = 0

    def poly_degree(self, widget, message, *args):
        widget.text = message[2]

    def selected_file(self, *args):
        self.source_file_path = args[1][0]

    def launch_plotting(self):
        if self.source_file_path is not "":
            plot_values(self.source_file_path)

        # todo
        #  make a popup for no file selected


class RootWidget(Widget):

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)


class DemoApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    DemoApp().run()