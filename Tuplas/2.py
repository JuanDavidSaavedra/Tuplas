
import os
from datetime import datetime

#Datafono
archivo = "Datafono.txt"
f = open(archivo, 'r')
linea = f.read()
y = []
y = linea.split(" ")
print(y)

datafonos = {1:2510, 2:2520, 3:2530, 4:2540}
tarjetas = {1:121802, 2:151803, 3:151804}

codigoDatafono = int(y[2])
CodigoTarjeta = int(y[0])
valor = int(y[1])

if valor >=0 and valor <=100000:
    comision = valor*0.005
if valor >100000 and valor <=1000000:
    comision = valor*0.004
if valor >1000000:
    comision = valor*0.01

#print("Valor a cobrar del manejo de la transacción: " + str(comision))

t1 = (datafonos[codigoDatafono], comision, valor-comision)
t2 = (tarjetas[CodigoTarjeta], valor)
print(t1)
print(t2)

f.close()
os.system("notepad.exe Datafono.txt")