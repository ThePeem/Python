### FUNCIONES Y ALCANCE ###

def suma(a, b):
    return a + b

print(suma(10, 5)) # 15

def otro(a,b):
    return

print(otro(10, 5)) # None

def funcion(a,b):
    def sumas(a,b):
        return a + b
    return sumas(a,b)

print(funcion(10, 5)) # 15

#  variable LOCAL y GLOBAL

