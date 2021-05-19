"""
Author: Edgar
Fecha: May-13-21
Desc: aprendizaje con dicts
"""
# Asi se inicializa un dict vacio.


class PersonalInfo(object):
    
    personal_info = {}

    def set_name(self, name: str) -> dict:
        personal_info['name'] = name
        return personal_info

    def set_last_name(self, last_name: str) -> dict:
        pass

    def set_age(self, age: int) -> dict:
        pass

    def get_information(self) -> str:
        pass


if __name__ == '__main__':
    personal_info = {}
    print('Diccionario declarado, antes de comenzar a llenarlo:', personal_info)
    # para añadir datos a un diccionario primero se usa el nombre de la variabl,
    # seguido de la key entre corchetes y se iguala con el value (valor) deseado
    name = input('Cual es tu nombre: ')
    personal_info['name'] = name
    print('Diccionario ya con el oprimer dato que es el nombre:', personal_info)
    personal_info['last_name'] = 'Ocampo'
    print(personal_info)
    personal_info['age'] = 34
    personal_info['hobbies'] = ['music', 'basket', 'videogames']
    print('La informacion personal es:', personal_info)
    # metodo pop del dict.
    personal_info.pop('hobbies')
    print(personal_info)
    print('name: ', personal_info['name'])
    print('name: ', personal_info.get('name'))
    personal_info.popitem()
    print(personal_info)
    
