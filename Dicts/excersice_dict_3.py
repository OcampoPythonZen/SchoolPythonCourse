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


personal_info_test = {
    "first_name": "Edgar",
    "last_name": "Ocampo",
    "age": 34,
    "subjects": [
        {
            "subject_name": "Redes neuronales",
            "rate": 80.0,
            "approved": True,
            "excelent": "improve yourself, you can"
        },
        {
            "subject_name": "IA Introduccion",
            "rate": 60.0,
            "approved": False,
            "excelent": "improve yourself, you can"
        },
        {
            "subject_name": "Tensorflow",
            "rate": 100.0,
            "approved": True,
            "excelent": "EXCELENT"
        }
    ],
    "subjects_number": 3,
    "subjects_mean": 80.0
}


class Academy(object):

    personal_info = {}
    subject_context = {}
    subjects = []

    def get_information(self) -> dict:
        name = input('Whats your name? ')
        self.personal_info['name'] = name.capitalize()
        last_name = input('Whats your last name? ')
        self.personal_info['last_name'] = last_name.capitalize()
        age = int(input('What old are you? '))
        self.personal_info['age'] = age
        len_subjects = int(
            input('How many subjects would you add into the register? '))
        for sub in range(len_subjects):
            print(f'Position: {sub} and values: {self.subjects}')
            subject_to_add = input('What is the name of the subject? ')
            self.subject_context['subject_name'] = subject_to_add.title()
            rate_to_add = float(input('What is the rate of this subject? '))
            self.subject_context['rate'] = rate_to_add
            self.subject_context['approved'] = True if self.subject_context.get(
                'rate') >= 70 and self.subject_context.get('rate') <= 100 else False
            self.subject_context['excelent'] = 'excelent' if self.subject_context.get(
                'rate') >= 100 else 'impprove yourself, you can.'
            self.subjects.append(self.subject_context.copy())
        self.personal_info['subjects'] = self.subjects
        self.personal_info['subjects_number'] = len(self.subjects)
        rates = []

        rates_2 = [sub['rate'] for sub in self.subjects]
        print('for inline: ', rates_2)
        for sub in self.subjects:
            rates.append(sub.get('rate'))
        self.personal_info['mean'] = mean(rates)
        return self.personal_info


if __name__ == '__main__':
    academy = Academy()
    print(academy.get_information())


'''
{1} =  Alumno, se dea agregar mas informacion o borrarla
{} = Como inserto o hago la logica para tener todos los datos de los alumnos y
representar la informacion general como resumen a la escuela o directora.. 

'''
