
import math

def test_my_cart():
    # I will test with a list
    # print is a function to show in monitor or console something
    my_market_list = []
    new_product = input('Add a new product in your list:')
    my_market_list.append(new_product)
    second_product = input('Add a second product in you list:')
    my_market_list.append(second_product)
    print('You have these product on your market list', my_market_list)
    print('Were gonna erase or delete an item of your list...')
    my_market_list.pop()
    print(my_market_list)


def my_data_types():
    # My data types vars
    my_string = 'myText'
    pi = math.pi
    version = 12
    my_list = [1, 2, 3, 4, 5, 6, 7, 9, 0, 3, 4545, 4545, 23, 1, 12, 34, 232]
    print(type(my_string))  # this kinf of type is str
    print(type(pi))  # this kind of type is float
    print(type(version))  # this kinf of type is int
    print(type(my_list))  # this kind of type is list


def vars_like_these():
    # Make 4 vars like these
    my_string_2 = 'Thi is my second str'
    float_number = 9.99
    my_age = 33
    my_list_2 = ['Sabina', 'Edgar', 'Chucho', 'Emiliano', 'Bertha', 'Juan']
    print(my_string_2)
    print(float_number)
    print(my_age)
    for nombre in my_list_2:
        if 'Sabina' == nombre:
            print('She is in the current team.')
        else:
            print('She does not here in the current team.')


if __name__ == "__main__":
    test_my_cart()

