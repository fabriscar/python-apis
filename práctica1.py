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

#Ejercicio 6
nombre = input("Nombre: ")
edad = int(input("Edad: "))
print("Hola" + nombre + "el año que viene vas a tener " + str(edad+1) + " años")

#Ejercicio 7
nums = [10,20,30]
for n in nums:
    print(n/2)
print(len(nums))


