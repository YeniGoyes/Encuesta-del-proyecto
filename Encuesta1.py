
n = 0
resultados = ""
while n < 10 :
    Nombre = input("Hola, ingresa tu nombre: ")
    Proyecto = input("Ingresa tu proyecto de programación: ")
    resultados = resultados + f"{Nombre}, su proyecto es {Proyecto}\n"
    n +=1
print(f"{resultados}")

