from encodings import mac_iceland
import requests
from datetime import datetime
import json

url = "https://api.open-meteo.com/v1/forecast"
params = {"latitude": -31.42, "longitude": -64.18, "current_weather": "true", "timezone": "America/Argentina/Cordoba"}

def leer_json(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) :
        return []

try: 
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    datos = r.json()
    actual = datos["current_weather"]
    temperatura = actual["temperature"]
    viento = actual["windspeed"]
    registro = {
    "consulta": datetime.now().isoformat(),
    "temperatura": temperatura,
    "viento": viento,
    }
    historial = leer_json("clima.json")      # lee lo que ya había (o [] si no existe)
    historial.append(registro)               # agrega la consulta nueva
    with open("clima.json", "w", encoding="utf-8") as f:
        json.dump(historial, f, indent=2, ensure_ascii=False)
    print(registro)
    print(f"Córdoba: {temperatura} °C, viento {viento} km/h")
except requests.exceptions.RequestException as e:
    print("No pude consultar el clima:", e)