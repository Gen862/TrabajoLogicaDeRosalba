#un individuo desea invertir su capital en un banco y desea saber cuanto dinero ganar despues de un mes
#si el banco paga a razon el 2% mensual
cap_inv=float(input("digite su capital de inversion: "))
gan= cap_inv*0.02
print(gan)

'''Un vendedor recibe un sueldo base mas un 10% extra por comision de ventas, el vendedor desea saber
cuanto dinero obtendra por concepto de comisiones por las tres ventas que realiza en el mes y el total que
recibira en el mes tomando en cuenta su sueldo base y comisiones'''

sueldo_b=float(input("Digite su sueldo fijo: "))
v1=float(input("Digite el monto de la venta numero 1: "))
v2=float(input("Digite el monto de la venta numero 2: "))
v3=float(input("Digite el monto de la venta numero 3: "))
tot_venta=v1+v2+v3
comisiones=(tot_venta*0.10)
tpag=sueldo_b+comisiones
print(f"el total a pagar es: {tpag} y las comisiones fueron {comisiones}")

#una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber
#cuanto debera pagar finalmente por su compra
total_compra=float(input("Digite el total de la compra: "))
desc=total_compra*0.15
tp=total_compra*desc
print(tp)

'''Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se 
compone de los siguientes porcentajes:
55% del promedio de sus tres calificaciones parciales.
30% de la calificación del examen final. 
15% de la calificación de un trabajo final'''

c1=float(input("Digite la primera calificación: "))
c2=float(input("Digite la segunda calificación: "))
c3=float(input("Digite la tercera calificación: "))
ef=float(input("Digite el valor del examen final: "))
tf=float(input("Digite la nota del trabajo final: "))
prom=(c1+c2+c3)/3
ppar=prom*0.55
pef=ef*0.30
ptf=tf*0.15
cf=ppar+pef+ptf
print(f"El valor de la calificación final es: {cf}")

#Un maestro desea saber que porcentaje de hombres y que porcentaje de mujeres hay en un grupo de estudiantes

hombre=int(input("Ingrese numero de hombres: "))
mujer=int(input("Ingrese numero de mujeres: "))
ta=hombre+mujer
porcH=(hombre*100)/ta
porcM=(mujer*100)/ta
print(f"La Cantidad de hombre en porcentaje es: {porcH} y la Cantidad de mujeres en porcentaje es: {porcM}")

#Realizar un algoritmo que calcule la edad de una persona

fechaNac=int(input("Ingrese año en el que nació 'ejemplo 1993': "))
actualFe=int(input("Ingrese fecha del año actual: "))
edad=fechaNac-actualFe
print(f"Al Dia de hoy tienes: {edad} años de edad")