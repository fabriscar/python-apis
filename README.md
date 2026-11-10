# python-apis

Ejercicios y mini proyectos de Python con APIs.

## clima.py
Consulta el clima actual de Córdoba a la API pública Open-Meteo
y guarda cada consulta en `clima.json`, con fecha y hora.

### Qué hace
- Hace un GET a la API con `requests` (con timeout).
- Maneja errores de red y de la API sin romperse.
- Guarda un historial de consultas en un archivo JSON.

### Cómo correrlo
1. `py -m venv venv` y activar el entorno
2. `pip install requests`
3. `py clima.py`

### Qué aprendí
Aprendí y sigo aprendiendo el manejo de lectura y escritura con JSON, me costó armar la estructura para el diccionario del clima, pero finalmente pude.
