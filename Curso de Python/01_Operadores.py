### OPERADORES Y ESTRUCTURAS DE CONTROL ###

# Operadores simples

print(10 + 5) # Suma
print(10 - 5) # Resta
print(10 * 5) # Multiplicación
print(10 / 5) # División
print(10 % 5) # Módulo
print(10 ** 5) # Exponenciación
print(10 // 5) # División entera

# Operadores de comparación

print(10 == 5) # Igualdad
print(10 != 5) # Desigualdad
print(10 > 5) # Mayor que
print(10 < 5) # Menor que
print(10 >= 5) # Mayor o igual que
print(10 <= 5) # Menor o igual que

# Operadores lógicos

print(True and False) # AND
print(True or False) # OR
print(not True) # NOT

# Estructuras de control

# Condicional if

if 10 > 5:
    print("10 es mayor que 5")

# Condicional if-else

if 10 < 5:
    print("10 es menor que 5")
else:
    print("10 no es menor que 5")

# Condicional if-elif-else

if 10 < 5:
    print("10 es menor que 5")
elif 10 == 5:
    print("10 es igual a 5")
else:
    print("10 no es menor que 5 ni igual a 5")

# Bucle for

for i in range(10):
    print(i)

# Bucle while

i = 0
while i < 10:
    print(i)
    i += 1

# Bucle infinito

while True:
    print("Hola Python")
    break

# Bucle infinito con condición

i = 0
while True:
    print(i)
    i += 1
    if i == 10:
        break

# Bucle infinito con condición y continue

i = 0
while True:
    i += 1
    if i % 2 == 0:
        continue
    print(i)
    if i == 10:
        break

