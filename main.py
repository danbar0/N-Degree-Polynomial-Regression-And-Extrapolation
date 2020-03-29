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

<SaveFile>:
    title: 'Save File'

    # FileChooserLayout
    BoxLayout:
        orientation: 'vertical'

        # ButtonArea
        BoxLayout:
            orientation: 'horizontal'
            spacing: 50
            size_hint: (.5,.5)
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            FileChooserListView:
                on_selection: 
                    app.root.selected_file(*args)

<RootWidget>:

''')


class SaveFile(Popup):
    pass


class RootWidget(BoxLayout):

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        filepop = SaveFile()
        filepop.open()

    def selected_file(self, *args):
        print("args=", args[1])
        plot_values(args[1][0])


class DemoApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    DemoApp().run()