#JSON es texto con un formato fijo para guardar listas y diccionarios. Python tiene dos funciones principales: una para guardar tus datos en un archivo y otra para leerlos de vuelta.
#guardar datos en un archivo json --> json.dump(datos, archivo)
#leer datos de un archivo json --> json.load(archivo)

#Ejercicio 1
import ensurepip
import json
personas = [
    {"nombre":"Fabri","edad":21, "ciudad":"Córdoba"},
    {"nombre":"Fabri1","edad":21, "ciudad":"Jujuy"},
    {"nombre":"Fabri2","edad":24, "ciudad":"Salta"},
    {"nombre":"Fabri3","edad":23, "ciudad":"BsAs"}
]

with open("personas.json", "w", encoding="utf-8") as f:
    json.dump(personas, f, indent=2, ensure_ascii=False)

#Ejercicio 2
with open("personas.json", "r", encoding="utf-8") as f:
    datos = json.load(f)

for p in datos:
    print(p["nombre"])

#Ejercicio 3
def edad_max(datos):
    maxima = 0
    for p in datos:
        if p["edad"] > maxima:
            maxima = p["edad"]
    return maxima
print(edad_max(datos))

#Ejercicio 4
datos.append({"nombre":"Anto", "edad":20, "ciudad":"Córdoba"})
with open("personas.json", "w", encoding="utf-8") as f:
    json.dump(datos, f, indent=2, ensure_ascii=False)

#Ejercicio 5
with open("resumen.txt", "w", encoding="utf-8") as f:
    for p in datos:
        f.write(f"{p['nombre']} ({p['edad']}) - {p['ciudad']}\n")

#Ejercicio cierre
with open("persona.json", "w", encoding="utf-8") as f:
    json.dump(personas, f, indent=2, ensure_ascii=False)

with open("personas.json", "r", encoding = "utf-8") as f:
    dato = json.load(f)

for p in dato:
    print(p["ciudad"])