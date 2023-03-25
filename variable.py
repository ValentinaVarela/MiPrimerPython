Num = 23
num1 = 1.25
valor = "hola"
v1 = True
print(type(num1))

#Operaciones Basicas
dato1 = 4
dato2 = 2
potenciacion = dato1**dato2
print("El resultado de la operacion es:", potenciacion)

dato1 = 40
dato2 = 2
division = dato1//dato2
print(f"El resultado de la operacion es {division}")

dato1 = int(input("Ingrese un numero:"))
dato2 = int(input("Ingrese un numero:"))
division = dato1//dato2
print("el resultado es %d" % (division))

#metodos lower(), upper(), title()
texto = "hola grupo!!"
print(texto.upper())    
print(texto.lower())  
print(texto.title())  

#Actividad 1
totalhoras = 6
preciohora = 1000
multiplicar = totalhoras*preciohora
print("la hora de llegada es a las 8 y la hora de salida es a las 2 pagaria:", multiplicar)

horallegada = 8
horasalida = 12
preciohora = 3500
totalhoras = horasalida - horallegada
total = preciohora * totalhoras
print("El valor hora es", totalhoras, "total hora", total)

#Actividad 2
dato1 = int(input("Ingrese un numero:"))
dato2 = int (input("Ingrese un numero:"))
division = dato1 // dato2
residuo = dato1 % dato2
"""print("su dividendo es %d" % (dato1))
print("su divisor es %d" % (dato2))
print("su cociente es %d" % (division))
print("su residuo es %d" % (residuo))"""
print(f"\tcociente {dato1//dato2}\n\tresiduo {dato1%dato2} \n\tdividendo {dato1} \n\tdivisor {dato2}")