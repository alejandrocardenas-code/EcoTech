import urequests

def enviar_dato(api_key, valor):
    url = "https://api.thingspeak.com/update?api_key={}&field1={}".format(api_key, valor)
    
    try:
        response = urequests.get(url)
        response.close()
    except:
        print("Error enviando a ThingSpeak")