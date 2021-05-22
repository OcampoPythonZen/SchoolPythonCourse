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

from statistics import mean
edgar_info_inicial = {
    "nombre": "Edgar",
    "apellido": "Ocampo",
    "edad": 34,
    "materias": [
        {
            "nombre_materia": "Redes neuronales",
            "calificacion": 80.0
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


class Academy(object):

    def get_information(self) -> dict:
        personal_info = {} 
        subject_context = {} 
        subjects = []
        name = input('Whats your name? ')
        personal_info['name'] = name.capitalize()
        last_name = input('Whats your last name? ')
        personal_info['last_name'] = last_name.capitalize()
        age = int(input('What old are you? '))
        personal_info['age'] = age
        len_subjects = int(
            input('How many subjects would add into register? '))
        for subject in range(len_subjects):
            subject_to_add = input('What is the name of the subject? ')
            subject_context['subject_name'] = subject_to_add.title()
            rate_to_add = float(input('What is the rate of this subject? '))
            subject_context['rate'] = rate_to_add
            subject_context['approved'] = False if subject_context.get('rate') >= 70 and subject_context.get('rate') <=100 else False
            subjects.append(subject_context)
        personal_info['subjects'] = subjects
        personal_info['subjects_number']= len(subject_context.get('subjects'))
        personal_info['mean'] = mean()
        return personal_info

    def __str__(self) -> str:
        return f'{self.nombre.capitalize()} estos son tus materias que agregaste. {self.materias}'


if __name__ == '__main__':
    academy = Academy()
    print(academy.get_information())


'''
{1} =  Alumno, se dea agregar mas informacion o borrarla
{} = Como inserto o hago la logica para tener todos los datos de los alumnos y
representar la informacion general como resumen a la escuela o directora.. 

'''