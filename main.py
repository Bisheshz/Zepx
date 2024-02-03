from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.button import MDFloatingActionButtonSpeedDial
from kivy.uix.textinput import MDTextInput

class BisheshApp(MDApp):
    def build(self):
        layout = MDFloatLayout()

        # Text input for displaying captured Python code
        self.python_code_input = MDTextInput(
            hint_text="Captured Python Code",
            size_hint=(0.8, 0.2),
            pos_hint={"center_x": 0.5, "center_y": 0.7},
            readonly=True
        )
        layout.add_widget(self.python_code_input)

        # Floating action button (FAB) with the letter "B" icon
        fab = MDFloatingActionButtonSpeedDial(
            icon="alpha-b",
            bg_hint_color=(1, 0, 0, 1),
            data={"B": "alpha-b"},
            rotation_root_button=True,
            pos_hint={"center_x": 0.5, "center_y": 0.3},
            rotation_root_button_color=self.theme_cls.primary_color,
            rotation_root_button_mode="label",
            rotation_root_button_font_size="40sp",
            rotation_root_button_label="Bishesh"
        )
        fab.bind(on_release=self.capture_python_code)
        layout.add_widget(fab)

        return layout

    def capture_python_code(self, instance):
        # For demonstration, let's set a sample captured Python code
        python_code = "print('Hello, Bishesh!')"
        self.python_code_input.text = python_code

if __name__ == "__main__":
    BisheshApp().run()
