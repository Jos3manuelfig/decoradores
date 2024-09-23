def funcionExterna(nombre):
    def envoltura():
        print("inicio de la funcion")
        print(nombre)
        print("Fin de la funcion")
    return envoltura


mi_funcion = funcionExterna("jose Manuel")
mi_funcion()

