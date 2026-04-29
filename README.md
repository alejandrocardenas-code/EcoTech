# EcoTech 

EcoTech es un sistema IoT diseñado para el monitoreo y control de condiciones ambientales en espacios urbanos, enfocado en el cuidado de plantas mediante la recolección de datos en tiempo real y la automatización de procesos.

## Descripción

El sistema permite medir variables ambientales críticas como temperatura, humedad y concentración de CO₂, facilitando la supervisión del estado de las plantas. A partir de estos datos, se ejecutan acciones automáticas, como la activación de sistemas de riego o ventilación, optimizando las condiciones del entorno.

Adicionalmente, los datos son enviados a una plataforma en la nube para su almacenamiento y análisis.

## Funcionalidades

* Medición de temperatura y humedad mediante sensor DHT22
* Monitoreo de concentración de CO₂ con sensor MQ135
* Visualización de datos en pantalla OLED
* Envío de datos a la plataforma ThingSpeak
* Automatización de actuadores (riego o ventilación)
* Monitoreo continuo en tiempo real

## Tecnologías utilizadas

* MicroPython
* ESP32
* ThingSpeak
* Sensores ambientales (DHT22, MQ135)
* Pantalla OLED SSD1306

## Arquitectura del sistema

El sistema está organizado en módulos independientes que permiten una mejor escalabilidad y mantenimiento:

```id="w8h2if"
EcoTech/
│
├── main.py
├── wifi.py
├── sensors.py
├── display.py
├── actuators.py
├── thingspeak_service.py
├── config.py
└── README.md
```

## Funcionamiento

1. El sistema se conecta a una red WiFi
2. Se capturan datos de temperatura, humedad y CO₂
3. Los datos se muestran en la pantalla OLED
4. Se evalúan condiciones ambientales
5. Se activan actuadores según los umbrales definidos
6. Los datos se envían a ThingSpeak para almacenamiento

## Instalación

1. Clonar el repositorio:

```id="7g6kaf"
git clone https://github.com/alejandrocardenas-code/EcoTech.git
```

2. Configurar las credenciales en el archivo `config.py`:

```id="mbkr8d"
WIFI_SSID = "tu_red"
WIFI_PASSWORD = "tu_password"
THINGSPEAK_API_KEY_CO2 = "tu_api_key"
THINGSPEAK_API_KEY_TEMP = "tu_api_key"
THINGSPEAK_API_KEY_HUM = "tu_api_key"
```

3. Cargar el código en el ESP32 utilizando MicroPython

4. Ejecutar el archivo `main.py`

## Ejemplos de uso

* Monitoreo de cultivos urbanos
* Control ambiental en azoteas verdes
* Automatización de riego básico
* Supervisión de calidad del aire

## Objetivo

El objetivo del proyecto es implementar una solución tecnológica que permita optimizar el cuidado de plantas en entornos urbanos, promoviendo prácticas sostenibles mediante el uso de sistemas inteligentes.

## Autor

Alejandro Cardenas

## Mejoras futuras

* Integración con aplicaciones móviles
* Panel de visualización web
* Implementación de análisis predictivo
* Integración de más sensores ambientales
