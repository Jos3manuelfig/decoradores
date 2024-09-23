from datetime import datetime

def imprimirFecha():
    print(datetime.now().strftime("%d-%m-%Y"))


def imprimirHora():
    print(datetime.now().strftime("%h:%m:%S"))


def funcionExterna(funcionInterna):
    def funcionEnvoltorio():
        print("inicio de la funcion")
        funcionInterna()
        print("fin de la fucion")
    return funcionEnvoltorio

# mostarFecha = funcionExterna(imprimirFecha)
# #     mostarHora = funcionExterna(imprimirHora)
# mostarFecha()
# print()
# mostarHora()
#

# @funcionExterna
# def saludar():
#     print("hola")
#
#
# saludar()
@funcionExterna
def imprimirFecha():
    print(datetime.now().strftime("%d-%m-%Y"))

imprimirFecha()
