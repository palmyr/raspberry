import adafruit_dht
import board
import time


class App:

    def __init__(self):
        self.dhtDevice = adafruit_dht.DHT11(board.D4)

    def init(self):

        while True:
            try:
                # Print the values to the serial port
                temperature_c = self.dhtDevice.temperature
                temperature_f = temperature_c * (9 / 5) + 32
                humidity = self.dhtDevice.humidity
                print(
                    "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                        temperature_f, temperature_c, humidity
                    )
                )
            except RuntimeError as error:
                # Errors happen fairly often, DHT's are hard to read, just keep going
                print(error.args[0])
                time.sleep(2.0)
                continue
            except Exception as error:
                self.dhtDevice.exit()
                raise error
            time.sleep(2.0)


if __name__ == "__main__":
    App().init()
