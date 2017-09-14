from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class MilesToKilometresConvert(App):
    def build(self):
        Window.size = (400, 200)
        self.title = "Miles to Kilometres Converter"
        self.root = Builder.load_file('m_to_km_convert.kv')
        return self.root

    def handle_calculate(self):
        miles = self.get_valid_input()
        kilometres = miles * 1.60934
        self.root.ids.output_label.text = str(kilometres)

    def handle_increment(self, increment):
        display = self.get_valid_input() + increment
        self.root.ids.input_miles.text = str(display)
        self.handle_calculate()

    def get_valid_input(self):
        try:
            user_input = float(self.root.ids.input_miles.text)
            return user_input
        except ValueError:
            return 0.0

MilesToKilometresConvert().run()
