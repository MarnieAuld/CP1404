from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label


class NameLabelling(App):
    def build(self):
        self.title = "Strings to Name Labels"
        self.root = Builder.load_file('name_labeling.kv')
        return self.root

    def create_widgets(self):
        names = ["Adam", "Barry", "Craig", "David", "Emma"]
        for name in names:
            temp_label = Label(text=name)
            self.root.ids.entriesBox.add_widget(temp_label)

NameLabelling().run()
