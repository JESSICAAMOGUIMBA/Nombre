import time,os
import turtle
#segundos
"""
for x in range (1,61):
	print(x)
"""
# reloj
"""
while True:
	t=time.localtime()
	os.system ("cls")# revisar el os
	print(str(t[3])+ ":"+str(t[4])+ ":"+str(t[5]))
	time.sleep(0.5)"""

t= turtle # con ejercicio estrella impar
t= turtle.Pen()
"""
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)"""
"""
     #ejercicio
t.reset()
for x in range(1,12):
	t.forward(100)
	t.left(250)
#turtle.getscreen()._root.mainloop()"""
#ejercicio


"""
		#ejercicio
t.reset()
for x in range(0,6):
	t.forward(45)#angulo
	t.left(45)#angulo"""

		#ejercicio
"""
def micuadrado (size):
	for x in range (1,5):
		t.forward(size)
		t.left(90)

turtle.getscreen()._root.mainloop()"""

		# estrella par
"""
def estrellapar(tamano,n):
	for i in range(n):
		t.forward(tamano)
		t.left(angulo)
print ("\t Estrella Par")
tamano= int(input("Ingrese el tamaño para la estrella:  "))
n= int(input("ingrese un numero par: "))

angulo =(-360/n)+180
estrellapar(tamano,n)"""

		# estrella impar

numeroLados = int(input("\tIngresar num,ero impar de lados de poligono:  "))
angulo= (-(360/numeroLados+180)*2)
def estrella(size):
	for x in range (1,(numeroLados+1)):
		t.forward(300)
		t.left(size)
t.reset()
estrella(angulo)
turtle._getscreen()._root.mainloop()








