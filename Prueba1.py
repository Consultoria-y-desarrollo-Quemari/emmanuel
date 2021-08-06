# 1. Genera un script que lea un carácter, determine y escriba si es:
# • letra mayúscula consonante --> ok
# • letra minúscula consonante --> ok
# • letra mayúscula vocal --> ok
# • letra minúscula vocal --> ok
# • dígito --> ok
# • operador aritmético --> ok
# • signo de puntuación --> ok
# • carácter especial. --> ok

# ex. input = script("A")
def script(input):
    vocaleslower = "aeiou"
    vocalesupper = "AEIOU"
    oper_arit = "+-*/"
    sign_punt = "´.;,:¨"
    car_espe = "!#$%&/()=?¡"
    if input.isalpha() is True:
        if input.islower() is True:
            if any(x in vocaleslower for x in input):
                tipo = "Letra Minúscula Vocal"
            else:
                tipo = "Letra Minúscula Consonante"
        elif input.isupper() is True:
            if any(x in vocalesupper for x in input):
                tipo = "Letra Mayúscula Vocal"
            else:
                tipo = "Letra Mayúscula Consonante"
    elif input.isnumeric() is True:
        tipo = "Dígito"
    else:
        if any(x in oper_arit for x in input):
            tipo = "Operador Artimético"
        elif any(x in sign_punt for x in input):
            tipo = "Signo de Puntuación"
        elif any(x in car_espe for x in input):
            tipo = "Caractér Especial"
        else:
            tipo = "Desconocido"
    return tipo

