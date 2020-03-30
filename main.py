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

Builder.load_string('''
#:kivy 1.10.0

<PolynomialPowerSelector>:
    FloatLayout:
        pos_hint:   {'center_x': 0.3, 'center_y': 0.9}
        
        Button:
            pos_hint:   {'center_x': 0.25, 'center_y': 0.25}
            size_hint:  .05, .05
            text:       '+'
            
        Button:
            pos_hint:   {'center_x': 0.3, 'center_y': 0.25}
            size_hint:  .05, .05
            text:       '-'
            
        Label:
            pos_hint:   {'center_x': 0.4, 'center_y': 0.25}
            size_hint:  .05, .05
            text:       'test'
        
    
<SelectFile>:
    FloatLayout:
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
        
        SelectFile:
        PolynomialPowerSelector:
            
''')

class ExceptionPopup(Popup):

    def close_popup(self):
        pass


class PolynomialPowerSelector(FloatLayout):

    def poly_degree(self, widget, message, *args):
        widget.text = message[2]


class SelectFile(FloatLayout):

    def selected_file(self, *args):
        plot_values(args[1][0])




class RootWidget(Widget):

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)


class DemoApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    DemoApp().run()