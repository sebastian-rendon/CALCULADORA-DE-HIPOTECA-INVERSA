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


        self.resultado_monto_mensual = Label(text="La cuota mensual aparecerá aquí", color=(0, 1, 0, 1))

        self.resultado_total_acumulado = Label(text="El total acumulado aparecerá aquí", color=(0, 1, 0, 1))

        self.resultado_saldo_proyectado = Label(text="El saldo proyectado aparecerá aquí", color=(0, 1, 0, 1))

        layout.add_widget(Label(text="Valor de la vivienda:"))
        layout.add_widget(self.valor_vivienda_input)

        layout.add_widget(Label(text="Tasa de interés anual (%):"))
        layout.add_widget(self.tasa_interes_input)

        layout.add_widget(Label(text="Plazo del crédito (años):"))
        layout.add_widget(self.plazo_input)

        layout.add_widget(Label(text="Porcentaje LTV (%):"))
        layout.add_widget(self.porcentaje_LTV_input)

        layout.add_widget(Label(text="Edad del propietario:"))
        layout.add_widget(self.edad_input)

        

        layout.add_widget(Label(text="Cuota mensual:"))
        layout.add_widget(self.resultado_monto_mensual)
        layout.add_widget(Label(text="Total acumulado:"))
        layout.add_widget(self.resultado_total_acumulado)
        layout.add_widget(Label(text="Saldo proyectado:"))
        layout.add_widget(self.resultado_saldo_proyectado)


        layout.add_widget(calcular_button)
        return layout
    
    def calcular(self, sender):
        # Obtener los datos ingresados por el usuario y realizar los cálculos correspondientes
        # utilizando la lógica de la calculadora de hipoteca inversa. Luego, actualizar las 
        # etiquetas de resultado con los valores calculados.

        print("Se realizaron los respectivos calculos")

        valor_inmueble = int(self.valor_vivienda_input.text)
        tasa_capitalizacion = float(self.tasa_interes_input.text)
        plazo_simulacion = int(self.plazo_input.text)
        porcentaje_LTV = float(self.porcentaje_LTV_input.text)
        edad = int(self.edad_input.text)
        resultado = credito(valor_inmueble=valor_inmueble, tasa_capitalizacion=tasa_capitalizacion, plazo_simulacion=plazo_simulacion, porcentaje_LTV=porcentaje_LTV, edad=edad)


        result_monto_mensual = calculadora_hipoteca_inversa.calcular_monto_mensual_recibido(resultado)
        result_total_recibido = calculadora_hipoteca_inversa.calcular_total_recibido_acumulado(resultado)
        result_saldo_proyectado = calculadora_hipoteca_inversa.calcular_saldo_proyectado(resultado)
        
        self.resultado_monto_mensual.text = f"${result_monto_mensual:.0f}"
        self.resultado_total_acumulado.text = f"${result_total_recibido:.0f}"
        self.resultado_saldo_proyectado.text = f"${result_saldo_proyectado:.0f}"

        print(f"El monto mensual recibido es: {result_monto_mensual}")
        print(f"El total recibido acumulado es: {result_total_recibido}")
        print(f"El saldo proyectado es: {result_saldo_proyectado}")
    
if __name__ == '__main__':
    HipotecaInversaGUI().run()