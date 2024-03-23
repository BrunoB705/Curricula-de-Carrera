#TAMBIEN TENGO ESTE CODIGO:


import sqlite3
import json


conn = sqlite3.connect('base_de_datos.db')


cursor = conn.cursor()


estado_materias = {
    "CDIV": ("r",13),
    "GAL 1":("r",9),
    
    "Prog. 1": ("r",10),
    "GAL 2": ("r",9),
    "CDIVV": ("r",13),
    "MD 1": ("r",9),

    "Prog. 2": ("r",12),
    "MD 2": ("r",9),
    "Logica": ("r",12),
    "Prob. y Est.": ("r",10),

    "Prog. 3": ("r",15),
    "Met. Num": ("r",8),
    "Arqui. Comp": ("r",12),
    
    "Teo. Leng":("r",12),
    "I.I.O":("r",10),
    "Sist. Op":("r",12),
    "Prog. 4": ("r",15),

    "Redes Compt":("r",12),
    "F. Base Datos":("r",15),
    "T. Prog":("r",15),

    "Prog. Func":("r",10),
    "I.I.S":("r",4),
    "Prog. Log":("r",10),

    "P.I.S":("r",15)
}




previas = {
    "CDIVV": {"CDIV": ["a", "e"]},
    "GAL 2": {"GAL 1": ["a", "e"]},
    "MD 2": {"MD 1": ["a", "e"]},
    "Prob. y Est.": {"CDIV": ["e"], "GAL 1": ["e"], "CDIVV": ["a", "e"]},
    "Logica": {"MD 1": ["a", "e"]},
    "Prog. 2": {"Prog. 1": ["a", "e"]},

    "Met. Num":{"CDIVV":["e"],"CDIV":["e"],"GAL 1":["e"],"GAL 2":["e"],"Prog. 1":["e"]},
    "Arqui. Comp":{"CDIV":["e"],"Prog. 1":["e"],"Logica":["a","e"],"MD 1":["a","e"],"Prog. 2":["a","e"]},
    "Prog. 3":{"Prog. 2":["a","e"],"Prog. 1":["e"],"MD 1":["e"]},

    "Teo. Leng":{"CDIV":["e"],"Logica":["e"],"GAL 1":["e"],"MD 1":["e"],"Prog. 3":["a","e"]},
    "Prog. 4": {"Prog. 1": ["e"], "Prog. 2": ["e"],"MD 1":["e"],"CDIV":["e"],"GAL 1":["e"]},
    "Sist. Op":{"CDIV":["e"],"Prog. 2":["e"],"MD 1":["e"],"GAL 1":["e"],"Arqui. Comp":["a","e"]},
    "I.I.O":{"GAL 1":["e"],"CDIV":["e"],"CDIVV":["e"],"GAL 2":["e"],"Prob. y Est.":["e"]},

    "Redes Compt":{"CDIV":["e"],"Prog. 3":["e"],"Arqui. Comp":["a","e"],"Sist. Op":["a","e"]},
    "F. Base Datos":{"Logica":["e"],"MD 2":["e"],"Prog. 3":["e"]},
    "T. Prog":{"Prog. 3":["e"],"Prog. 4":["a","e"]},

    "Prog. Func":{"Prog. 2":["e"],"Logica":["e"],"Teo. Leng":["e"],"MD 1":["e"]},
    "I.I.S":{"F. Base Datos":["a","e"],"T. Prog":["a","e"],"Prog. 4":["a","e"]},
    "Prog. Log":{"MD 2":["e"],"Logica":["e"],"Teo. Leng":["e"],"Prog. 3":["e"]},

    "P.I.S":{"Prog. 4":["e"],"I.I.S":["a","e"]}

}

# Crear la tabla de EstadoMaterias
cursor.execute('''CREATE TABLE EstadoMaterias (
                    materia TEXT PRIMARY KEY,
                    estado TEXT,
                    creditos INTEGER
                )''')

# Crear la tabla de Previas con la columna estados_previa
cursor.execute('''CREATE TABLE Previas (
                    materia TEXT,
                    previa TEXT,
                    estados_previa TEXT,
                    FOREIGN KEY (materia) REFERENCES EstadoMaterias(materia),
                    FOREIGN KEY (previa) REFERENCES EstadoMaterias(materia)
                )''')
cursor.execute('''CREATE TABLE CreditosTotales(
               creditosT INTEGER
)''')
cursor.execute('INSERT INTO CreditosTotales (creditosT) VALUES (?)',(0,))
# Insertar datos en la tabla EstadoMaterias
for materia,(estado, creditos) in estado_materias.items():
    cursor.execute('INSERT INTO EstadoMaterias (materia, estado,creditos) VALUES (?, ?, ?)', (materia, estado, creditos))


# Insertar datos en la tabla Previas
for materia, prerequisitos in previas.items(): # materia es la key, prerequisitos es el value
    for previa, estados in prerequisitos.items(): #previa es la key, estados es el value
        # Convertir la lista de estados en una cadena JSON
        estados_json = json.dumps(estados)

        cursor.execute('INSERT INTO Previas (materia, previa, estados_previa) VALUES (?, ?, ?)', (materia, previa, estados_json))



conn.commit()
conn.close()

