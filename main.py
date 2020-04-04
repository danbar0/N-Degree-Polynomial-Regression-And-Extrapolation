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
from kivy.lang import Builder
from kivy.graphics import *

Builder.load_string('''
#:kivy 1.10.0
#:import Factory kivy.factory.Factory

<StartButton>:
    FloatLayout:
        Button:
            pos_hint:   {'center_x': 0.3, 'center_y': 0.25}
            size_hint:  (0.1, 0.1)
            text:       '-'
            

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
            on_release: root.popup_reference.create_popup_with_text("test")
            
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
            on_selection:   root.set_selected_file(*args)
            
<MessagePopup>:
    title: 'Message'
    title_size: 30
    title_align: 'center'
    size_hint: (None, None)
    size: 400, 400
    
    BoxLayout:
        orientation: 'vertical'
        padding: 10
            
        Label:
            text: root.message_text
        
        Button: 
            text: 'Close'
            size_hint: 0.8, 0.2
            pos_hint: {'x': 0.1, 'y': 0.1}
            on_release: root.dismiss()
    
                
<RootWidget>:
    FloatLayout:
        size: root.size
        pos: root.pos
        
        SelectionMenu:
            
''')


class MessagePopup(Popup):
    message_text = ""
    def create_popup_with_text(self, message):
        # box = BoxLayout(orientation='vertical', padding=10)
        # popup = Popup(title="Message",
        #                 title_size=30,
        #                 title_align='center',
        #                 content=box,
        #                 size_hint=(None, None),
        #                 size=(400, 400))
        #
        # box.add_widget(Label(text=message, text_size=(box.center_x,box.center_y)))
        #
        # box.add_widget(Button(text="Close",
        #                 size_hint=(0.8, 0.2),
        #                 pos_hint={"x":0.1, "y":0.1},
        #                 on_release=popup.dismiss))
        self.message_text = message
        popup = MessagePopup()
        # popup = Popup(title="Message",
        #                 title_size=30,
        #                 title_align='center',
        #                 content=show,
        #                 size_hint=(None, None),
        #                 size=(400, 400))
        popup.open()


class SelectionMenu(FloatLayout):
    popup_ref = MessagePopup()

    def __init__(self, **kwargs):
        super(SelectionMenu, self).__init__(**kwargs)
        self.source_file_path = ""
        self.polynomial_degree = 0

    def poly_degree(self, widget, message, *args):
        widget.text = message[2]

    def set_selected_file(self, *args):
        self.source_file_path = args[1][0]

    def launch_plotting(self):
        if self.source_file_path is not "":
            plot_values(self.source_file_path)
        else:
            self.popup_ref.create_popup_with_text("Please select a source file before running")


class RootWidget(Widget):

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)


class DemoApp(App):
    def build(self):
        return RootWidget()


if __name__ == '__main__':
    DemoApp().run()