from statistics import mean
data = {
    "nombre": "Edgar",
    "apellido": "Ocampo",
    "edad": 34,
    "materias": [
        {
            "nombre_materia": "Redes neuronales",
            "calificacion": 80.0,
            "aprobado": True
        },
        {
            "nombre_materia": "IA Introduccion",
            "calificacion": 60.0,
            "aprobado": False
        },
        {
            "nombre_materia": "Tensorflow",
            "calificacion": 100.0,
            "aprobado": True
        }
    ],
    "numero_materias": 3,
    "promedio_general": 80.0
}

calificaciones=[]
for sub in data['materias']:
    print('rate: ', sub['calificacion'])
    calificaciones.append(sub['calificacion'])
    print()

print('Mean: ', mean(calificaciones))


