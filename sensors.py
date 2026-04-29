from machine import Pin, ADC
import dht

# DHT22
sensor_dht = dht.DHT22(Pin(4))

# CO2 (MQ135)
co2_sensor = ADC(Pin(35))
co2_sensor.atten(ADC.ATTN_11DB)
co2_sensor.width(ADC.WIDTH_12BIT)

def leer_temperatura_humedad():
    sensor_dht.measure()
    return sensor_dht.temperature(), sensor_dht.humidity()

def leer_co2():
    valor = co2_sensor.read()
    ppm = (valor / 4096) * 5000
    return ppm