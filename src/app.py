import adafruit_dht


class App:

    def init(self):
        temperature = self.dht_device.temperature
        humidity = self.dht_device.humidity

        print(f"{temperature} {humidity}")


if __name__ == "__main__":
    App().init()
