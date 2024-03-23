from tkinter import *
import sqlite3
from funciones import cambiar,restablecerBD,cerrarApp


root = Tk()
root.geometry("1200x680")
root.title("Malla Curricular")

root.pack_propagate(False)

def cambiar_creditos(event, botones):
    cambiar(event, botones)
    conn = sqlite3.connect('base_de_datos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT creditosT FROM CreditosTotales')
    creditos_actuales = cursor.fetchone()[0]
    creditosLabel.config(text=f"Creditos: {creditos_actuales}")
    

# ESTE COLOR PUEDE ESTAR BUENO: #fab5af PARA EL TRANSPARENTE

#estados posibles:  'reprobado','aprobado','exonerado'

botones = {}



# COMIENZO FILA 1 
fila1 = Frame(root,bg="#f59b84",height=640/8)
fila1.pack_propagate(False)
fila1.pack(side=TOP,fill=X)

filaCreditos = Frame(fila1,bg="gray",height=30,width=80)
filaCreditos.pack_propagate(False)
filaCreditos.pack(side=LEFT)

creditosLabel = Label(filaCreditos,text=f"Creditos: 0",width=50,height=20)
creditosLabel.pack(side=TOP)

# COMIENZO BOTONES DE FILA 1
boton11 = Button(fila1, text=f"P.I.S",bg="#de1b1b",fg="white",width=10,height=2,borderwidth=5)
boton11.pack(side=LEFT, padx=478, pady=10)
botones["P.I.S"] = boton11



# FILA 12
fila12 = Frame(root,bg="#f5af84",height=640/8)
fila12.pack_propagate(False)
fila12.pack(side=TOP,fill=X)


boton12 = Button(fila12,text="Prog. Func",bg="#de1b1b",fg="white",width=10,height=2,borderwidth=5)
boton12.pack(side='left',padx=186, pady=10)
botones["Prog. Func"] = boton12


boton13 = Button(fila12,text="I.I.S",bg="#de1b1b",fg="white",width=10,height=2,borderwidth=5)
boton13.pack(side='left',padx=100, pady=10)
botones["I.I.S"] = boton13


boton14 = Button(fila12,text="Prog. Log",bg="#de1b1b",fg="white",width=10,height=2,borderwidth=5)
boton14.pack(side='right',padx=160, pady=10)
botones["Prog. Log"] = boton14

# FIN BOTONES DE FILA 1
# FIN FILA 1



# COMIENZO FILA 2

fila2 = Frame(root,bg="#f5cd84",height=640/8)
fila2.pack_propagate(False)
fila2.pack(side=TOP,fill=X)

# COMIENZO BOTONES DE FILA 2
boton21 = Button(fila2, text=f"Redes Compt",bg="#de1b1b",fg="white",width=10,height=2,borderwidth=5)
boton21.pack(side="left",padx=182, pady=10)
botones["Redes Compt"] = boton21




boton22 = Button(fila2,text="F. Base Datos",bg="#de1b1b",fg="white",width=10,height=2,borderwidth=5)
boton22.pack(side="left",padx=106, pady=10)
botones["F. Base Datos"] = boton22


boton23 = Button(fila2,text="T. Prog",bg="#de1b1b",fg="white",width=10,height=2,borderwidth=5)
boton23.pack(side="right",padx=156, pady=10)
botones["T. Prog"] = boton23





# COMIENZO FILA 21

fila21 = Frame(root,bg="#f5e684",height=640/8)
fila21.pack_propagate(False)
fila21.pack(side=TOP,fill=X)
# COMIENZO BOTONES FILA 21

boton24 = Button(fila21,text="I.I.O",bg="#de1b1b",fg="white",width=10,height=2,borderwidth=5)
boton24.pack(side='left',padx=106, pady=10)
botones["I.I.O"] = boton24


boton25 = Button(fila21,text="Teo. Leng",bg="#de1b1b",fg="white",width=10,height=2,borderwidth=5)
boton25.pack(side='left',padx=106, pady=10)
botones["Teo. Leng"] = boton25


boton26 = Button(fila21,text="Sist. Op",bg="#de1b1b",fg="white",width=10,height=2,borderwidth=5)
boton26.pack(side='left',padx=106, pady=10)
botones["Sist. Op"] = boton26


boton27 = Button(fila21,text="Prog. 4",bg="#de1b1b",fg="white",width=10,height=2,borderwidth=5)
boton27.pack(side='left',padx=106, pady=10)
botones["Prog. 4"] = boton27
#boton24.bind("<Button-1>", cambiar)

# FIN BOTONES DE FILA 2

# FILA 3
fila3 = Frame(root,bg="#f5db84",height=640/8)
fila3.pack_propagate(False)
fila3.pack(side=TOP,fill=X)
# BOTONES FILA 3
# COMIENZO BOTONES DE FILA 2
boton31 = Button(fila3, text=f"Met. Num",bg="#de1b1b",fg="white",width=10,height=2,borderwidth=5)
boton31.pack(side="left",padx=182, pady=10)
botones["Met. Num"] = boton31



boton32 = Button(fila3,text="Arqui. Comp",bg="#de1b1b",fg="white",width=10,height=2,borderwidth=5)
boton32.pack(side="left",padx=106, pady=10)
botones["Arqui. Comp"] = boton32


boton33 = Button(fila3,text="Prog. 3",bg="#de1b1b",fg="white",width=10,height=2,borderwidth=5)
boton33.pack(side="right",padx=156, pady=10)
botones["Prog. 3"] = boton33




# FILA 31
fila31 = Frame(root,bg="#f5cd84",height=640/8)
fila31.pack_propagate(False)
fila31.pack(side=TOP,fill=X)
# BOTONES FILA 31
boton36 = Button(fila31,text="Prob. y Est.",bg="#de1b1b",fg="white",width=10,height=2,borderwidth=5)
boton36.pack(side='left',padx=106, pady=10)
botones["Prob. y Est."] = boton36


boton37 = Button(fila31,text="Logica",bg="#de1b1b",fg="white",width=10,height=2,borderwidth=5)
boton37.pack(side='left',padx=106, pady=10)
botones["Logica"] = boton37


boton38 = Button(fila31,text="MD 2",bg="#de1b1b",fg="white",width=10,height=2,borderwidth=5)
boton38.pack(side='left',padx=106, pady=10)
botones["MD 2"] = boton38


boton39 = Button(fila31,text="Prog. 2",bg="#de1b1b",fg="white",width=10,height=2,borderwidth=5)
boton39.pack(side='left',padx=106, pady=10)
botones["Prog. 2"] = boton39


# FILA 4
fila4 = Frame(root,bg="#f5af84",height=640/8)
fila4.pack_propagate(False)
fila4.pack(side=TOP,fill=X)
# BOTONES FILA 4
boton41 = Button(fila4,text="CDIVV",bg="#de1b1b",fg="white",width=10,height=2,borderwidth=5)
boton41.pack(side='left',padx=106, pady=10)
botones["CDIVV"] = boton41


boton42 = Button(fila4,text="GAL 2",bg="#de1b1b",fg="white",width=10,height=2,borderwidth=5)
boton42.pack(side='left',padx=106, pady=10)
botones["GAL 2"] = boton42


boton43 = Button(fila4,text="MD 1",bg="#de1b1b",fg="white",width=10,height=2,borderwidth=5)
boton43.pack(side='left',padx=106, pady=10)
botones["MD 1"] = boton43


boton44 = Button(fila4,text="Prog. 1",bg="#de1b1b",fg="white",width=10,height=2,borderwidth=5)
boton44.pack(side='left',padx=106, pady=10)
botones["Prog. 1"] = boton44


# FILA 41
fila41 = Frame(root,bg="#f59b84",height=640/8)
fila41.pack_propagate(False)
fila41.pack(side=TOP,fill=X)

# BOTONES FILA 41
boton44 = Button(fila41,text="CDIV",bg="#de1b1b",fg="white",width=10,height=2,borderwidth=5)
boton44.pack(side='left',padx=206, pady=10)
botones["CDIV"] = boton44


boton45 = Button(fila41,text="GAL 1",bg="#de1b1b",fg="white",width=10,height=2,borderwidth=5)
boton45.pack(side='right',padx=206, pady=10)
botones["GAL 1"] = boton45

# FILA AUXILIAR

filaAux = Frame(root,bg="#e3debc",height=100)
filaAux.pack_propagate(False)
filaAux.pack(side=BOTTOM,fill=X)

descripEx = Label(filaAux,text="EXONERADO",bg="GREEN",font=("Verdana",15))
descripEx.pack(side=LEFT,padx=10)

descripApr = Label(filaAux,text="APROBADO",bg="blue",font=("Verdana",15))
descripApr.pack(side=LEFT,padx=10)

descripRep = Label(filaAux,text="REPROBADO",bg="red",font=("Verdana",15))
descripRep.pack(side=LEFT,padx=10)

botonR = Button(filaAux,text="REINICIAR",bg="#cdcbd6",width=10,height=1,font=("Arial",12))
botonR.pack(side="right",padx=15)
def restablecer(botones):
    restablecerBD(botones)
    nuevos_Creditos = 0
    creditosLabel.config(text=f"Creditos: {nuevos_Creditos}")

botonR.bind("<Button-1>", lambda event: restablecer(botones))


for boton in botones.values():
    boton.bind("<Button-1>", lambda event: cambiar_creditos(event, botones))
    
root.protocol("WM_DELETE_WINDOW", lambda: cerrarApp(root,botones))

root.iconbitmap('assets/book_3725.ico')
root.mainloop()
