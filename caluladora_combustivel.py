from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class CalculadoraCombustivel(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10)

        # Pergunta: Qual seu combustível?
        layout.add_widget(Label(text="Qual seu combustível?"))
        alcool_button = Button(text="Álcool")
        gasolina_button = Button(text="Gasolina")
        alcool_button.bind(on_press=self.selecionar_combustivel)
        gasolina_button.bind(on_press=self.selecionar_combustivel)
        layout.add_widget(alcool_button)
        layout.add_widget(gasolina_button)

        # Pergunta: Qual o valor do combustível?
        layout.add_widget(Label(text="Qual o valor do combustível?"))
        self.valor_combustivel_input = TextInput(multiline=False)
        layout.add_widget(self.valor_combustivel_input)

        # Botão para calcular
        calcular_button = Button(text="Clique aqui para calcular")
        calcular_button.bind(on_press=self.calcular)
        layout.add_widget(calcular_button)

        self.result_label = Label(text="")
        layout.add_widget(self.result_label)

        self.combustivel_selecionado = None

        return layout

    def selecionar_combustivel(self, instance):
        self.combustivel_selecionado = instance.text

    def calcular(self, instance):
        try:
            preco_do_combustivel = float(self.valor_combustivel_input.text)
            combustivel_oposto = "Gasolina" if self.combustivel_selecionado == "Álcool" else "Álcool"
            print(combustivel_oposto)
            
            
            if self.combustivel_selecionado == "Álcool":
                self.result_label.text = f"{combustivel_oposto} tem que estar acima de R$ {preco_do_combustivel/0.7:.2f} para o álcool valer a pena"
            elif self.combustivel_selecionado == "Gasolina":
                self.result_label.text = f"{combustivel_oposto} tem que estar acima de R$ {preco_do_combustivel*0.7:.2f} para a gasolina valer a pena"
        except ValueError:
            self.result_label.text = "Por favor, insira um valor válido para o combustível"


if __name__ == "__main__":
    CalculadoraCombustivel().run()
