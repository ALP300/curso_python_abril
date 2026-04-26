'''
numero1=10
numero2=2
numero3= int(input("Ingresa un numero: "))
numero4= int(input("Ingresa otro numero: "))
numeros=[23,2,32,3,24,32,432,4,234,234,234]
print(numeros)
suma2= numero3+numero4
print("El primer número es",numero3,"y el segundo es", numero4)
print(f"El primer numero es: {numero3} y el segundo es: {numero4}")
print(f"Esta es la suma con inputs: {suma2}")
modulo= numero1%numero2
division= numero1/numero2
resta= numero1-numero2
sumaTotal= modulo+division
print("Esta es la suma total: ",sumaTotal)

#LISTAS
numeros=[23,32,32,3,24,32,432,4,234,234,234]
barcelona=["Gavi","Pedri","De Jong","Lewandoski"]
liverpool=["Salah","Van Dijk","Alisson","McAllister"]
n= int(input("Ingresa un número: "))
numeros.append(n)
#print(f"Los mejores mediocampistas son: {barcelona[1]} y {liverpool[3]}")
print("El número ingresado por la persona es: ",numeros[-1])

print(numeros)

equipoDeFutbol= {"Barcelona": ["Gavi","Pedri","De Jong","Lewandoski"], "Liverpool": ["Salah","Van Dijk","Alisson","McAllister"]}
equipoDeFutbol["Real Madrid"]= ["Benzema","Vinicius","Modric","Kroos"]
print(equipoDeFutbol["Barcelona"])
print(equipoDeFutbol)
'''
#DICCIONARIOS
diccionarioDeIngles={"casa": "house", "perro": "dog", "gato": "cat"}
diccionarioDeIngles["mesa"]="table"
print(diccionarioDeIngles)
print(diccionarioDeIngles["mesa"])
#else if
nota=19
if(nota>=18):
    print("Beca")
elif(nota>=15):
    print("Media beca")
elif(nota>=12):
    print("Pequeña beca")
else:
    print("No tienes beca")




numeros=(2,4,5,6,7)
numeros.append(77)
print(numeros)
