from machine import Pin, ADC

class PinState:
    def __init__(self, pin: int, mode: any) -> None:
        self.pin = Pin(pin, mode)
        self.state = 0

    def on(self):
        self.pin.on()
        self.state = 1

    def off(self):
        self.pin.off()
        self.state = 0

    def get_state(self):
        return self.state


class State:
    def __init__(self) -> None:
       
        self.bomb = PinState(5, Pin.OUT)
        self.humidity_sensor = Pin(16, Pin.IN)
        self.temperature_sensor = ADC(0)

    def get_humidity(self):
        return self.humidity_sensor.value()

    def get_temperature(self):
        raw_value = self.temperature_sensor.read()
        temperature = raw_value * (3.3 / 1023.0) * 100 
        return round(temperature, 2)

state = State()
