#Diccionarios: guardan pares clave:valor, son como los objetos JSON
#len(persona) --> cuenta las claves
#Casi cualquier API devuelve una lista de diccionarios

persona = {"nombre": "Ana", "edad": 20}

print(persona["nombre"])         # Ana
persona["ciudad"] = "Córdoba"    # agrega una clave nueva
persona["edad"] = 21             # modifica una existente
print(len(persona))              # 3: cuenta las claves
print("edad" in persona)         # True: pregunta si existe la clave
print(persona.get("telefono", "sin dato"))   # "sin dato", sin error

for clave, valor in persona.items():
    print(clave, valor)

#Funciones se definen con "def", llevan dos puntos, el cuerpo va identado y devuelven con return
def saludar(nombre):
    return f"Hola {nombre}"

def promedio(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)

print(saludar("Fabri"))
print(promedio([4,6,8]))

#La diferencia entre print y return: print muestra algo en pantalla, return devuelve el valor para que lo uses después, por ejemplo x = promedio([1, 2]).

#Ejercicio 1
def es_mayor(edad):
    if edad >= 18:
        return True
    return False

#Ejercicio 2
def contar_pares(lista):
    contar = 0
    for i in lista:
        if i%2 == 0:
            contar += 1
    return contar

print(contar_pares([1,2,3,4]))

#Ejercicio 3
productos={"pan": 800,"leche": 1200, "yerba": 3500}
total = 0
for c, v in productos.items():
    print(c + " cuesta " + str(v))
    total += v
    print(total)

#Ejercicio 4
alumnos=[
    {"nombre": "Fabrizio", "nota": 21},
    {"nombre": "Franco", "nota": 22},
    {"nombre": "Antonella", "nota": 23}
]

def promedio_notas(alumnos):
    total = 0
    for i in alumnos:
        total += i["nota"]
    return total/len(alumnos)

print(promedio_notas(alumnos))

#Ejercicio cierre de clase
def maxima(dicc):
    maxima = 0
    for i in dicc:
        if i["edad"] > maxima:
            maxima = i["edad"]
    return maxima


