import time
from wifi import connect_wifi
from sensors import *
from display import mostrar_datos
from actuators import *
from thingspeak_service import enviar_dato
from config import *

wifi = connect_wifi(WIFI_SSID, WIFI_PASSWORD)

if wifi:
    print("Sistema iniciado")

    while True:
        temp, hum = leer_temperatura_humedad()
        co2 = leer_co2()

        print("Temp:", temp, "Hum:", hum, "CO2:", co2)

        mostrar_datos(temp, hum, co2)

        # Control automático
        if temp > TEMP_LIMITE:
            activar()
        else:
            desactivar()

        # Enviar datos
        enviar_dato(THINGSPEAK_API_KEY_CO2, co2)
        enviar_dato(THINGSPEAK_API_KEY_TEMP, temp)
        enviar_dato(THINGSPEAK_API_KEY_HUM, hum)

        time.sleep(5)