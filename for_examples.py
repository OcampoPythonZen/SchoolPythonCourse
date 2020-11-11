
def len_of_my_name():
    # Length of my Name and display every character of it.
    # nulls values in python are None
    my_name = 'Edgar Omar'
    print('Len of my name:', len(my_name))
    for letter in my_name:
        print(letter)


def range_var_a():
    # Range var range(intial_value, final_value-, step_value)
    a = range(1, 50, 5)
    print('Printing the a var')
    for number in a:
        print(number)


def range_var_b():
    b = range(1, 10, 2)
    print('Printing the b var')
    for num in b:
        print(num)


def range_var_c():
    c = range(5)
    print('Printing the c var')
    for n in c:
        print(n)


def range_var_d():
    d = range(0, 6)
    print('Printing the d var')
    for numm in d:
        print(numm)
        print('***')


def nested_loops():
    # Nested loops
    for i in range(3):
        print('+...first_loop', 'position:', i)
        for j in range(2):
            print('-...second_loop', 'position:', j)


# How to declare a function on python language, put the keyword def after it choose a functions name
# put the parhentesis and the last put the :
def the_last_function():
    for i in range(1,11):
        print(i)

def my_fun_main():
    print('La casa o el inicio')

if __name__ == "__main__":
    import time
    # How to call the function on python language
    # just call fot its name of the function with theris ()
    #the_last_function()
    #the_last_function()
    print('Este es le menu pricipal')
    my_fun_main()
    print('elegiste una opcion')
    time.sleep(3)
    my_fun_main()

    