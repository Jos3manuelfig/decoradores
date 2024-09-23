
def OperarconPares(operacion):
    def envoltura(*args, **kwargs):
        soloPar = list(filter(lambda  num: num %2 ==0, args))
        resultado = operacion(*soloPar, **kwargs)
        print(f" el resultado de la operacion es: {resultado}")

        if 'estado' in kwargs:
            print(f"El estado es: {kwargs['estado']}")
        else:
            print("No se proporcionó el estado.")
            return resultado
    return envoltura

@OperarconPares
def sumarNumeros(*args, **kargs):
    acc = 0
    for num in args:
        acc +=num
    return  acc


sumarNumeros(1,2,3,4,5,6,estado = True)