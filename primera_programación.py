import tkinter as tk
from tkinter import messagebox
import random

def saludar():
    nombre_usuario = entrada_texto.get()
    if nombre_usuario:
        messagebox.showinfo("saludo", f"¡Hola {nombre_usuario}! Bienvenida a tu app.")
        barra_estado.config(text=f"saludos enviados a {nombre_usuario}")
    else    :
        messagebox.showinfo("saludo", "¡por favor , escribe tu nombre primero!")
def limpiar_texto():
    entrada_texto.delete(0, tk.END)
    barra_estado.config(text="listo")
    
def cambiar_color():
    colores=["#F0F3F4", "#E8F8F5", "#FEF9E7", "#FBEEE6", "#EAF2F8"]
    color_aleatorio= random.choice(colores)
    ventana.config(bg=color_aleatorio)
    etiqueta.config(bg=color_aleatorio)
    barra_estado.config(text="¡color de fondo cambiado!")
ventana= tk.Tk()
ventana.title("mi super app")
ventana.geometry("350x350")
etiqueta=tk.Label(ventana,text="Escribe tu nombre:", font="Arial 12 bold")
etiqueta.pack(pady=15)
entrada_texto=tk.Entry(ventana,font=("Arial",11),justify="center",width=25)
entrada_texto.pack(pady=5)
boton_saludo=tk.Button(ventana,text="¡salúdame!", command=saludar, bg="#2ecc71",fg="white", font=("Arial",10,"bold"))
boton_saludo.pack(pady=10, ipadx=15, ipady=5)
boton_limpiar=tk.Button(ventana, text="Borrar texto",command=limpiar_texto, bg="#e74c3c", fg="white")
boton_limpiar.pack(pady=5,ipadx=10)
boton_color=tk.Button(ventana, text="cambiar color de fondo", command=cambiar_color , bg="#3498db", fg="white")
boton_color.pack(pady=15,ipadx=10)
barra_estado=tk.Label(ventana, text="listo", bd=1,relief=tk.SUNKEN, anchor=tk.W,font=("Arial",9,"italic"))
barra_estado.pack(side=tk.BOTTOM, fill=tk.X)
ventana.mainloop()
   