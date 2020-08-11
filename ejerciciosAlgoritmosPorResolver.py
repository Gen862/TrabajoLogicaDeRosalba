#Dada la cantidad en pesos, obtener el equivalente en dolares asumiendo
#que la cantidad de cambio es desconocida

print("Bienvenido a la casa de cambios del dolar de hoy\n")
pesos=float(input("Digite el monto en pesos colombianos a calcular: "))
dolar=float(input("Ingrese la tasa actual del dolar hoy: "))
resultado=(pesos*dolar)/100
print(f"El resultado es: {resultado}")

#Sacar presupuesto anual para un hospital si en las tres areas se van un
#40% ginecologia, 30% pediatria, 30% traumatologia. cual seria el monto para las areas segun el capital

print("Bienvenido al calculador de capital")
monto=int(input("Digite el monto de capital de inversion anual para el hospital"))
gin=monto*0.40
pedi=monto*0.30
trau=monto*0.30
print(f"El capital para invertir en ginecologia es: {gin}, El capital para pediatria es: {pedi} y para trumatismo es de: {trau}")

'''El dueño de una tienda compra un articulo a un precio determinado, obtener el precio en que lo debe
vender para obtener una ganancia del 30%'''

articulo=float(input("Digite el precio del articulo: "))
gan=0.30
porc=articulo*gan
venta=articulo+porc
print(f"El producto tiene un precio de {articulo}, lo tienes que vender en: {venta} y tendras una ganancia neta de: {porc}")

'''Todos los lunes, miércoles y viernes, una persona corre la misma ruta y cronometra los 
tiempos obtenidos. Determinar el tiempo promedio que la persona tarda en recorrer la ruta en 
una semana cualquiera.'''

ruta=int(input("Digite la ruta en km que recorre por dia: "))
cronometro=float(input("Digite el tiempo en minutos, que se demora en correr esos km: "))
dias=3*ruta
tiem_prom=(dias*cronometro)/ruta
print(f"Te demoras en correr cada semana: {tiem_prom} minutos")

'''Tres personas deciden invertir su dinero para fundar una empresa. Cada una de ellas invierte 
una cantidad distinta. Obtener el porcentaje que cada quien invierte con respecto a 
la cantidad total invertida.'''

per1=int(input("Digite monto de inversion persona 1"))
per2=int(input("Digite monto de inversion persona 2"))
per3=int(input("Digite monto de inversion persona 3"))
cantidad=per1+per2+per3
print(f"La cantidad de inversion es: {cantidad}")
por1=(per1*100)/cantidad
por2=(per2*100)/cantidad
por3=(per3*100)/cantidad
print(f"La persona 1 invitio: {por1}%, la persona 2 invirtio: {por2}% y la persona 3 invirtio: {por3}%")

'''Un alumno desea saber cual será su promedio general en las
tres materias mas difíciles que cursa y cual será el promedio 
que obtendrá en cada una de ellas. Estas materias se evalúan como se muestra a continuación:

La calificación de Matemáticas se obtiene de la sig. manera:
Examen 90%
Promedio de tareas 10%
En esta materia se pidió un total de tres tareas.

La calificación de Física se obtiene de la sig. manera:
Examen 80%
Promedio de tareas 20%
En esta materia se pidió un total de dos tareas.

La calificación de Química se obtiene de la sig. manera:
Examen 85%
Promedio de tareas 15%
En esta materia se pidió un promedio de tres tareas.

'''
print("Bienvenido, evaluaremos la materia de Matemáticas")
tarea_mat1=float(input("Digite el monto de la tarea 1:"))
tarea_mat2=float(input("Digite el monto de la tarea 2:"))
tarea_mat3=float(input("Digite el monto de la tarea 3:"))
prom_tarea_mat=(tarea_mat1+tarea_mat2+tarea_mat3)/3*0.10
ex_mat=float(input("Digite la nota del examen final: "))
prom_exa_mat=ex_mat*0.90
matematica_nota_final=prom_exa_mat+prom_tarea_mat
print("La notal final de matematicas es: ",matematica_nota_final)
print("\nBienvenido de nuevo evaluaremos la materia de Fisica")
tarea_fisica1=float(input("Digite el monto de la tarea 1:"))
tarea_fisica2=float(input("Digite el monto de la tarea 2:"))
prom_tarea_fisica=(tarea_fisica1+tarea_fisica2)/2*0.20
ex_fis=float(input("Digite la nota del examen final: "))
prom_ex_fis=ex_fis*0.80
fisica_nota_final=prom_ex_fis+prom_tarea_fisica
print("La nota final de fisica es: ",fisica_nota_final)
print("\nBienvenido de nuevo evaluaremos la materia de Quimica")
tarea_Quim1=float(input("Digite el monto de la tarea 1:"))
tarea_Quim2=float(input("Digite el monto de la tarea 2:"))
tarea_Quim3=float(input("Digite el monto de la tarea 3:"))
prom_quim=(tarea_Quim1+tarea_Quim2+tarea_Quim3)/3*0.15
ex_quim=float(input("Digite la nota del examen final: "))
prom_ex_quim=ex_quim*0.85
quim_nota_final=prom_ex_quim+prom_quim
print("La nota final de Quimica es: ",quim_nota_final)











