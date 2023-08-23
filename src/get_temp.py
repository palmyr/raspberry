import adafruit_dht
from board import D4


class GetTemp:

    def get(self):
        dht_device = adafruit_dht.DHT11(D4)
        temperature = dht_device.temperature
        humidity = dht_device.humidity
        print(f"{temperature} {humidity}")


if __name__ == "__main__":
    GetTemp().get()