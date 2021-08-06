# 2. Genera un script que reciba una lista y ordene sus elementos de menor a mayor.

# ex. input = script("5,4,3,2,1")
def script(input):
    lista = input.split(",")
    lista.sort()
    return lista

