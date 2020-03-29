from extrapolation import plot_values

try:
    import kivy
except ImportError:
    raise ImportError("You don't have Kivy installed!")

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.lang import Builder

Builder.load_string('''
#:kivy 1.10.0

<SelectFile>:
    title: 'Modify parameters then select your source file'

    # FileChooserLayout
    BoxLayout:
        orientation: 'vertical'

        # ButtonArea
        FloatLayout:
            orientation: 'horizontal'
            spacing: 50

            FileChooserListView:
                size_hint: 0.5, 1
                pos_hint: {'center_x': 0.75, 'center_y': 0.5}
                on_selection: 
                    app.root.selected_file(*args)
                    
        #Polynomial Power
        FloatLayout:
            Button:
                pos_hint: {'center_x': 0.25, 'center_y': 0.25}
                size_hint: .2, .2
                text: 'Button 1'

<RootWidget>:

''')


class SelectFile(Popup):
    pass


class RootWidget(BoxLayout):

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        filepop = SelectFile()
        filepop.open()

    def selected_file(self, *args):
        plot_values(args[1][0])


class DemoApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    DemoApp().run()