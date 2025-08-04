from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty, BooleanProperty
from kivy.clock import Clock

class PainelIA(BoxLayout):
    status = StringProperty("Desligada")
    ameaca = NumericProperty(0)
    ia_ativa = BooleanProperty(False)

    def alternar_ia(self):
        self.ia_ativa = not self.ia_ativa
        if self.ia_ativa:
            self.status = "Ligada - Monitorando"
            Clock.schedule_interval(self.aumentar_ameaca, 1)
        else:
            self.status = "Desligada"
            Clock.unschedule(self.aumentar_ameaca)
            self.ameaca = 0

    def aumentar_ameaca(self, dt):
        if self.ameaca < 100:
            self.ameaca += 5

    def enviar_comando(self):
        comando = self.ids.campo_comando.text
        if comando.strip() == "":
            self.status = "Comando vazio"
        else:
            self.status = f"Executando: {comando}"
        self.ids.campo_comando.text = ""

class PainelApp(App):
    def build(self):
        return PainelIA()

if __name__ == "__main__":
    PainelApp().run()
