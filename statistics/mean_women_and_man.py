'''
Realizar un programa en python donde el usuario
indique la cantidad de usuario a registrar el nombre, la edad
y el sexo de cada una de las personas. Sacar promedio de las edades
de todos los usuario y ademas dar el porcentaje de hombres(m) y de mujeres(w).
Al final imprimir la tabla de los datos que se obtuvieron...
Todo hacerlo dentro de una clase...

Name        Age     Gender
---------------------------
Hector      12          m
Emiliano    13          m
Isao        12          m
Carlos      10          m
Sabina      11          w
Chucho      12          m
Edgar       34          m
--------------------------
'''
from statistics import mean

class MeanWomenAndMens(object):

    name_list = []
    age_list = []
    gender_list = []

    def fill_data(self, users: int)-> list:
        for user in range(users):
            name = input('Whats your name?:')
            self.name_list.append(name)
            age = int(input('How old are you?:'))
            self.age_list.append(age)
            gender = input('What is your gender: m(man) or w(woman)')
            self.gender_list.append(gender)

    def calculate_mean_age(self)-> int:
        return mean(self.age_list)

    def calculate_percentage_gender(self):
        pass

    def show_table_date(self):
        pass

if __name__ == '__main__':
    print('Main')