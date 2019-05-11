import time
from tkinter import *
tk= Tk()
canvas= Canvas(tk,width=300, height=300)#tamaño de la imagen
canvas.pack()
canvas.create_polygon(10,10,10,60,50,35)

for x in range(0,60):
	canvas.move(1,5,-1)#-1 cordenada de moviminto
	tk.update()
	time.sleep(0.05)

tk.mainloop()
