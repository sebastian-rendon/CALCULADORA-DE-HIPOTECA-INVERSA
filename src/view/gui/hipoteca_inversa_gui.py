import sys
sys.path.append("src")
from model.logica_calculohipoteca_comentado import credito, calculadora_hipoteca_inversa

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class HipotecaInversaGUI(App):
    def build(self):
        layout = GridLayout(cols=2)
        # Campos de entrada
        self.valor_vivienda_input = TextInput(hint_text="Valor de la vivienda")
        self.tasa_interes_input = TextInput(hint_text=("Tasa de interés anual (%)"))
        self.plazo_input = TextInput(hint_text="Plazo del crédito (años)")
        self.edad_input = TextInput(hint_text="Edad del propietario")
        self.porcentaje_LTV_input = TextInput(hint_text="Porcentaje LTV (%)")

        calcular_button = Button(text="Calcular")
        calcular_button.bind(on_press=self.calcular)

        self.resultado_label = Label(text="El resultado aparecerá aquí")

        layout.add_widget(Label(text="Valor de la vivienda:"))
        layout.add_widget(self.valor_vivienda_input)

        layout.add_widget(Label(text="Tasa de interés anual (%):"))
        layout.add_widget(self.tasa_interes_input)

        layout.add_widget(Label(text="Plazo del crédito (años):"))
        layout.add_widget(self.plazo_input)

        layout.add_widget(Label(text="Edad del propietario:"))
        layout.add_widget(self.edad_input)

        layout.add_widget(Label(text="Porcentaje LTV (%):"))
        layout.add_widget(self.porcentaje_LTV_input)
        
        layout.add_widget(calcular_button)

        return layout
    
    def calcular(self, sender):
        pass
    
if __name__ == '__main__':
    HipotecaInversaGUI().run()