# funciones.py
from tkinter import *
import sqlite3
import json


estado_materias = {"CDIV": "r","MD 1":"r", "CDIVV": "r","GAL 2":"r","MD 1":"r","Prog. 1":"r",
                   "Prob. y Est.":"r","Logica":"r","MD 2":"r","Prog. 2":"r",
                   "Met. Num":"r","Arqui. Comp":"r","Prog. 3":"r","Prog. 4": "r"}

previas = {"CDIVV": {"CDIV":["a","e"]},"GAL 2": {"GAL 1":["a","e"]}, 
           "MD 2":{"MD 1":["a","e"]}, "Prob. y Est.":{"CDIV":["e"],"GAL 1":["e"],"CDIVV":["a","e"]},
           "Logica":{"MD 1":["a","e"]},
           "Prog. 2":{"Prog. 1":["a","e"]}, "Prog. 4": {"Prog. 1": ["e"], "Prog. 2": ["e"]}}

# Lista de dependencias inversa para cada materia
dependencias_inversas = {}
for materia, prerequisitos in previas.items():
    for prerequisito in prerequisitos:
        if prerequisito not in dependencias_inversas:
            dependencias_inversas[prerequisito] = []
        dependencias_inversas[prerequisito].append(materia)

def cambiar(event,botones):
    conn = sqlite3.connect('base_de_datos.db')
    cursor = conn.cursor()
    nombre = event.widget["text"]
    cursor.execute('SELECT * FROM EstadoMaterias WHERE materia = ?', (nombre,))
    resultado = cursor.fetchone()
    cursor.execute('SELECT creditosT FROM CreditosTotales')
    creditos_actuales = cursor.fetchone()[0]
    if resultado:
        materia,estado,credito = resultado
        if nombre == materia:
            if estado == 'r' and verificar_cumplimiento_previas(nombre):
                event.widget.config(bg="blue", fg="white")
                cursor.execute('UPDATE EstadoMaterias SET estado = ? WHERE materia = ?', ('a', nombre))
                conn.commit()
            if estado == 'a' and verificar_cumplimiento_previas(nombre):
                event.widget.config(bg="green",fg="white")
                cursor.execute('UPDATE EstadoMaterias SET estado = ? WHERE materia = ?', ('e', nombre))
                cursor.execute('UPDATE CreditosTotales SET creditosT = ?',(creditos_actuales + credito,))
                conn.commit()
            if estado == 'e':
                event.widget.config(bg="#de1b1b",fg="white")
                volver_rojo(nombre,botones)
                cursor.execute('UPDATE EstadoMaterias SET estado = ? WHERE materia = ?', ('r', nombre))
                cursor.execute('UPDATE CreditosTotales SET creditosT = ?',(creditos_actuales - credito,))
                conn.commit()
    conn.close()




def verificar_aprobado(curso,cursor):
    cursor.execute('SELECT estado from EstadoMaterias where materia = ?',(curso,))
    test = cursor.fetchone()
    return test[0]


def verificar_cumplimiento_previas(curso):
    conn = sqlite3.connect('base_de_datos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT previa,estados_previa from Previas WHERE materia = ?',(curso,))
    previas_resultado = cursor.fetchall()
    centinela = True
    faltaAprobar = []
    for nombre,estado in previas_resultado:
        estado_previa = json.loads(estado)
        estadoMateria = verificar_aprobado(nombre,cursor)
        if not estadoMateria in estado_previa:
            faltaAprobar.append(nombre)
            #print(f"No aprobado: {nombre,estadin}")
            centinela = False
    conn.close()
    if len(faltaAprobar) > 0:
        print("Falta aprobar o exonerar: ",faltaAprobar)
    return centinela       


def volver_rojo(curso,botones):
    conn = sqlite3.connect('base_de_datos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT materia,previa from Previas WHERE previa = ?',(curso,))
    materias_resultado = cursor.fetchall()
    if materias_resultado:
        for materia in materias_resultado:
            hacerRojo,previa = materia
            if materia[1] == curso:
                if hacerRojo in botones:
                    boton = botones[hacerRojo]
                    boton.config(bg="#de1b1b")
                    cursor.execute('UPDATE EstadoMaterias SET estado = ? WHERE materia = ?', ('r', hacerRojo))
                    conn.commit()
    conn.close()




def restablecerBD(botones):
    conn = sqlite3.connect('base_de_datos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT materia from EstadoMaterias')
    materias = cursor.fetchall()
    for materia in materias:
        cursor.execute('UPDATE EstadoMaterias SET estado = ? WHERE materia = ?', ('r', materia[0]))
    cursor.execute('UPDATE CreditosTotales SET creditosT = ?',(0,))
    conn.commit()
    conn.close()
    for boton in botones.values():
        boton.config(bg="#de1b1b")


def cerrarApp(root,botones):
    restablecerBD(botones)
    print("CERRO")
    root.destroy()
