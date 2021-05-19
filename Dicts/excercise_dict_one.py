'''
() -> tuple
[] -> list
{} -> dict, este es el tipo de dato que menos hemos visto
pero posiblemente uno de los mas que vamos a ocupar.
'Hello' -> str
3.14 -> float
0 -> int
'c' -> str
True -> bool
1 -> int
False -> bool
None -> NoneType
'''

cualquier_var = 89
listasnums = [1,2,3,4,5,6]
# dict{k:v, k:v, n...}
divisas_inter = {
    "dollar": "$",
    "euro" : "€",
    "yen" : "¥",
    "peso_colombiano" : "π",
    "pi": 3.14159,
    "lista_de_valor_divisas": [2.2, 3, 2.2, 'a', [1,2,3,4,5]],
    "otro" : "sin divisa."
    }
#La manera en llamar a los diccionarios es por la key y nos traera el value(s) de dicha key
#print("La operacion que se genero esta en dolares, su simbolo es: ", divisas_inter['dollar'])

# keys() contiene solo las claves de identificacion del dict
for divisa in divisas_inter.keys():
    print(divisa)

print('----separacion-----')

# values() contiene solo los valores del dict, sin las claves que lo identican
for divisa in divisas_inter.values():
    print(divisa)

print('----separacion-----')

# items() genera una tupla (tuple()) cn la clave y el valor de cada uno de los elementos del dict
for divisa in divisas_inter.items():
    print(divisa)
    