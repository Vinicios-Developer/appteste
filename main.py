import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from plyer import gps
from plyer import notification

kivy.require("1.11.1")


class GPSApp(App):

    def build(self):
        self.layout = BoxLayout(orientation="vertical")
        self.button = Button(text="Obter Localização", size_hint_y=None, height=50)
        self.button.bind(on_press=self.get_location)
        self.layout.add_widget(self.button)
        return self.layout

    def get_location(self, obj):
        try:
            gps.configure(on_location=self.on_location)
            gps.start()
        except NotImplementedError:
            notification.notify(
                title="GPS",
                message="GPS não disponível neste dispositivo.",
            )

    def on_location(self, **kwargs):
        lat = kwargs["lat"]
        lon = kwargs["lon"]
        notification.notify(
            title="Localização",
            message=f"Sua localização é: {lat}, {lon}",
        )


if __name__ == "__main__":
    GPSApp().run()
