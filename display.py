from machine import I2C, Pin
from ssd1306 import SSD1306_I2C

i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = SSD1306_I2C(128, 64, i2c)

def mostrar_datos(temp, hum, co2):
    oled.fill(0)
    oled.text("Temp: {} C".format(temp), 0, 0)
    oled.text("Hum: {} %".format(hum), 0, 16)
    oled.text("CO2: {:.2f}".format(co2), 0, 32)
    oled.show()
    