"""#Condicional if
#Ingresar edad del usuario, muestre si es mayor de edad.
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print(nombre, "Eres mayor de edad")
else:
    print("Eres menor de edad")
    
#elif
#elif condicion:
        #instruiccion
num1 = int(input("Ingrese numero:"))
num2 = int(input("Ingrese numero:"))
if num1>num2:
    print(num1, "Es mayor")
elif num1<num2:
    print(num2, "Es mayor")
else:
    print(f"{num1} y {num2} son iguales")"""
    
#Pedir al usuario la edad y a que grupo quiere pertenecer [adultos/infantes].si el usuario tiene 18 años o mas y si escoge adultso que muestre "Puede ingresar al grupo", de lo contrario "exede la edadpara pertenecer al grupo". si tiene menos de 18 y escoge infantes que muestre "Puede ingresar al grupo de infantes", de lo contrario "no puede ingresar". si escoge una opcion diferente debe salir OPCION NO VALIDA.

edad = int(input("Ingrese su edad: "))
grupo = input("¿A qué grupo quiere pertenecer [adultos/infantes]? ")

if grupo == "adultos":
    if edad >= 18:
        print("Puede ingresar al grupo.")
    else:
        print("Excede la edad para pertenecer al grupo.")
elif grupo == "infantes":
    if edad < 18:
        print("Puede ingresar al grupo de infantes.")
    else:
        print("No puede ingresar.")
else:
    print("Opción no válida.")