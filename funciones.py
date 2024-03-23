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

'''def cambiar(event, botones):
    global estado_materias
    curso = event.widget["text"]
    if not verificar_cumplimiento_previas(curso, estado_materias):
        return
    else:
        current_bg = event.widget.cget("bg")
        if current_bg == "#fab5af": # ESTE COLOR ES ROJO TRANSPARENTE
            event.widget.config(bg="blue", fg="white")
            estado_materias[curso] = "a"
            desbloquear(curso,botones)
        elif current_bg == "blue":
            event.widget.config(bg="green", fg="white")
            estado_materias[curso] = "e"
            desbloquear(curso,botones)
        elif current_bg == "green":
            event.widget.config(bg="#fab5af", fg="white")
            estado_materias[curso] = "r"
            
            volver_rojo(curso, botones)
    print(dependencias_inversas)
'''
'''def verificar_cumplimiento_previas(curso_seleccionado, estado_previas):
    global previas
    previas_curso = previas.get(curso_seleccionado, [])
    if isinstance(previas_curso, dict):
        for previa, estado in previas_curso.items():
            if estado_previas.get(previa) not in estado:
                print(f"No cumples con las previas necesarias para {curso_seleccionado}.")
                print(f"Estado actual de {previa}: {estado_previas.get(previa)}")
                return False
    print(f"Cumples con las previas necesarias para {curso_seleccionado}.")
    return True'''

'''def volver_rojo(curso, botones):
    global dependencias_inversas, estado_materias
    if curso in dependencias_inversas:
        for materia in dependencias_inversas[curso]:
            estado_materias[materia] = "r"
            boton = botones.get(materia)
            if boton:
                boton.config(bg="#fab5af", fg="white")
'''
'''def verificar_cumplimiento_previas(curso):
    conn = sqlite3.connect('base_de_datos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT previa,estados_previa from Previas WHERE materia = ?',(curso,))
    previas_resultado = cursor.fetchall()
    cursor.execute('SELECT materia,estado from EstadoMaterias')
    totalM = cursor.fetchall() # TOTAL MATERIAS
    estan = [] # ARREGLO DE LAS PREVIAS QUE PRECISA LA MATERIA
    for nombre,estado in previas_resultado:
        estan.append(nombre)
    print(previas_resultado)
    for nombre,estado in previas_resultado:
        estado_previa = json.loads(estado) # ESTO ME LO CAMBIA A FORMATO LISTA.
        print(nombre)
        print(estado_previa)
        #print(verificar_aprobado(nombre,cursor))
        for nameT,estadT in totalM:
            if nameT in estan:
                if estadT in estado_previa:
                    print(nameT," ",estadT," ",estado_previa)
                    estan.remove(nameT)
        if not verificar_aprobado(nombre,cursor) in estado_previa:
            #print(f"curso: {nombre} ",verificar_aprobado(nombre,cursor),"=?=", estado_previa)
            print("No cumples estas previas: ",estan)
            conn.close()
            return False

    conn.close()
    return True
'''
'''def verificar_cumplimiento_previas(curso):
    conn = sqlite3.connect('base_de_datos.db')
    cursor = conn.cursor()
    cursor.execute('SELECT previa,estados_previa from Previas WHERE materia = ?',(curso,))
    previas_resultado = cursor.fetchall()
    if previas_resultado:
        for previa in previas_resultado:
            nombrePrevia,estadoPrevia = previa # GAL1, ['a','e']
            cursor.execute('SELECT * FROM EstadoMaterias WHERE materia = ? AND estado IN (?,?)',(nombrePrevia,'a','e'))
            resultado = cursor.fetchone() # GAL1,e
            if resultado is None or not resultado[1] in estadoPrevia:
                print(f"NO APROBADO: {curso}") # ACA ME GUSTARIA MOSTRAR TODAS LAS PREVIAS QUE SE NECESITA APROBAR
                conn.close()
                return False

    conn.close()
    return True
'''