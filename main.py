from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class CalculatorApp(App):
    def build(self):
        self.title = "Calculator for Vaishu 💕"
        self.icon = "calculator_icon.png"
        self.operators = ['+', '-', '*', '/']
        self.last_was_operator = None
        self.last_button = None
        self.result = TextInput(font_size=40, readonly=True, halign="right", multiline=False)

        main_layout = BoxLayout(orientation="vertical")

        main_layout.add_widget(self.result)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', 'C', '+']
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    font_size=30,
                    on_press=self.on_button_press
                )
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equals_button = Button(
            text="=",
            font_size=30,
            on_press=self.on_solution
        )
        main_layout.add_widget(equals_button)

        return main_layout

    def on_button_press(self, instance):
        current = self.result.text
        button_text = instance.text

        if button_text == 'C':
            self.result.text = ''
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                return
            elif current == '' and button_text in self.operators:
                return
            else:
                new_text = current + button_text
                self.result.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.result.text
        if text:
            try:
                solution = str(eval(text))
                self.result.text = solution
            except Exception:
                self.result.text = "Error"


if __name__ == "__main__":
    CalculatorApp().run()
