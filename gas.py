from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class front(BoxLayout):
    def nowPrice(self, result, price, litro):
        p = float(price)
        l = float(litro)
        result.text = "{} Litros = R$ {:.2f}".format(l, p*l)

class what_gas(App):
    def build(self):
        return front()

what_gas().run()