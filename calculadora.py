import tkinter as tk
def presionar(num):
    pantalla.insert(tk.END,str(num))
def limpiar():
    pantalla.delete(0,tk.END)
def calcular():
    try:
        resultado = eval(pantalla.get())
        limpiar()
        pantalla.insert(tk.END, str(resultado))
    except:
        limpiar()
        pantalla.insert(tk.END, "Error")
ventana=tk.Tk()
ventana.title("calculadora")
ventana.configure(bg="blue") 
pantalla=tk.Entry(ventana, font=("Arial",20), bg="black",fg="white",bd=10, justify="right",relief=tk.FLAT) 
pantalla.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
botones=[
    ('C',1,0),('/',1,1),('*',1,2),('-',1,3),
    ('7',2,0),('8',2,1),('9',2,2),('+',2,3),
    ('4',3,0),('5',3,1),('6',3,2),('=',3,3),
    ('1',4,0),('2',4,1),('3',4,2),('0',4,3)
    ]
for(texto,fila,columna) in botones:
    if texto =='C':
        comando = limpiar
    elif texto =='=':
        comando= calcular
    else:
        comando=lambda x=texto: presionar(x)
    btn=tk.Button(ventana,text=texto,font=("Arial",14), bg="black",fg="white",width=5,height=2,relief=tk.FLAT,command=comando)
    btn.grid(row=fila,column=columna,padx=5,pady=5)
ventana.mainloop()