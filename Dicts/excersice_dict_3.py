'''
Escribir un programa en python que almacene la informacion en un formato de diccionario({})
dentro de python las materias que se imparten en la escuela AdvanceAcademy,

Materia(s) -> Alumno(s) ----- Alcance solo con los alumnos
Alumno(s) -> Profesor(es)

despues mostrar las materias y calificaciones con un rango minimo de 10 y un 
rango maximo de 100, siendo 70 la calificacion minima aprobatoria para identificar
que es un materia aprobada del alumno. 

Se podra preguntar si se desea consultar
todas las calificaciones de todas las materia o solo pedir la informacion de una 
materia. 

Decirle o mostrar  al alumno la cantidad de materias que tiene y mostrarle el promedio
en general de sus calificaciones ademas mostrar si la materia es aprobada o no. 
La informacion se debera mostrar en forma de tabla.

---------------------------------------------------------------------------------------
Nombre(s)   Apellidos(s)    Edad    Materia             Calificacion           Aprobado 
---------------------------------------------------------------------------------------
Edgar       Ocampo          34      Redes Neuronales        80                  True
Edgar       Ocampo          34      IA Introduccion         60                  False
Edgar       Ocampo          34      Tensorflow              100                 True
'''

edgar_info_inicial = {
    "nombre": "Edgar",
    "apellido": "Ocampo",
    "edad": 34,
    "materias": [
        {
            "nombre_materia": "Redes neuronales",
            "calificacion" : 80.0
        },
        {
            "nombre_materia": "IA Introduccion",
            "calificacion": 60.0
        },
        {
            "nombre_materia": "Tensorflow",
            "calificacion": 100.0
        }
    ]
}


edgar_info_resultado = {
    "nombre": "Edgar",
    "apellido": "Ocampo",
    "edad": 34,
    "materias": [
        {
            "nombre_materia": "Redes neuronales",
            "calificacion" : 80.0,
            "aprobado" : True
        },
        {
            "nombre_materia": "IA Introduccion",
            "calificacion": 60.0,
            "aprobado": False
        },
        {
            "nombre_materia": "Tensorflow",
            "calificacion": 100.0,
            "aprobado" : True
        }
    ],
    "numero_materias" : 3,
    "promedio_general": 80.0
}

print(edgar_info_resultado)
