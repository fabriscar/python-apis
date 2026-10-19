#Ejercicio 1
nombre = "Fabrizio"
edad = "21"
print("Me llamo " + nombre + " y tengo " + edad + " años")

#Ejercicio 2
n = int(input("Número: "))
if n%2 == 0:
    print("Par")
else:
    print("Impar")

#Ejercicio 3
lista = [1,2,3,4,5]
for i in lista:
    print(i * 2)

#Ejercicio 4
total = 0
for i in lista:
    total += i

print(total)

#Ejercicio 5
contar = [1,2,3,4,5,6,7,8,9,10]
for n in contar:
    if n%3 == 0:
        print("Salteado")
    else:
        print(n)