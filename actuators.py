from machine import Pin

rele = Pin(2, Pin.OUT)

def activar():
    rele.value(1)

def desactivar():
    rele.value(0)