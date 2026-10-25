#try/except te deja decir: “intentá esto, y si falla de esta manera, hacé esto otro en vez de caerte”.
from practica3 import personas
try:
    n = int("abc")
except ValueError:
    n = 0
    print("No es un número")
#Python intenta ejecutar lo que está dentro del try.
#Si no hay error, saltea el except por completo.
#Si hay un error del tipo que nombraste, salta al except y ejecuta eso.
#En los dos casos, el programa sigue después del bloque.
import json
try:
    with open("no_existe.json", "r", encoding="utf-8") as f:
        datos = json.load(f)
except FileNotFoundError:
    print("No encontré el archivo")
    datos = []

#Ejercicio 1
n = input("Numero: ")
try:
    n = int(n)
except ValueError:
    print("Eso no es un número")
    n = 0

#Ejercicio 2
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

print(dividir(1,0))

#Ejercicio 3
import json
def leer_json(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) :
        return []

print(leer_json("personas.json"))
datos = leer_json("personas.json")
print(datos)

t = 0
v = 0
with open("resumen.txt", "w", encoding="utf-8") as f:
    for p in datos:
        t += 1
        if "ciudad" not in p or "edad" not in p or "nombre" not in p:
            continue
        else:
            f.write(f"{p['nombre']} ({p['edad']}) - {p['ciudad']}\n")
            v += 1
print(f"Había {str(t)} personas, {str(v)} válidas")

    