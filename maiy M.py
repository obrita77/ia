from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty, BooleanProperty
from kivy.clock import Clock

class PainelIA(BoxLayout):
    status = StringProperty("Desligada")
    ameaca = NumericProperty(0)
    ia_ativa = BooleanProperty(False)
    _evento_ameaca = None  # Armazena o evento do Clock

    def alternar_ia(self):
        self.ia_ativa = not self.ia_ativa

        if self.ia_ativa:
            self.status = "Ligada - Monitorando"
            if not self._evento_ameaca:
                self._evento_ameaca = Clock.schedule_interval(self.aumentar_ameaca, 1)
        else:
            self.status = "Desligada"
            if self._evento_ameaca:
                self._evento_ameaca.cancel()
                self._evento_ameaca = None
            self.ameaca = 0

    def aumentar_ameaca(self, dt):
        if self.ameaca < 100:
            self.ameaca += 5
        else:
            self.status = "Ameaça máxima atingida!"
            if self._evento_ameaca:
                self._evento_ameaca.cancel()
                self._evento_ameaca = None

    def enviar_comando(self):
        comando = self.ids.campo_comando.text.strip()
        if not comando:
            self.status = " ⚠️ Comando vazio!"
        else:
            self.status = f"🛠 Executando: {comando}"
        self.ids.campo_comando.text = ""

class PainelApp(App):
    def build(self):
        return PainelIA()

if __name__ == "__main__":
    PainelApp().run()

