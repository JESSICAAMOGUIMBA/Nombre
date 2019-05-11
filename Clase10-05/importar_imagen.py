from tkinter import *
tk= Tk()
canvas= Canvas(tk,width=1204, height=768)#tamaño de la imagen
canvas.pack()

my_image = PhotoImage(file="Hydrangeas.gif")
canvas.create_image(50,50,anchor=NW, image=my_image)#50 50 para mover
tk.mainloop()