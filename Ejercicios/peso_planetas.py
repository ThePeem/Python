# Peso planetas

peso = float(input("¿Cuál es tu peso?"))

print("¿En qué planeta quieres saber tu peso?")
print("  1)Mercurio")
print("  2)Venus")
print("  3)Marte")
print("  4)Jupiter")
print("  5)Saturno")
print("  6)Urano")
print("  7)Neptuno")

planeta = int(input("(Indicar número)"))

if planeta == 1:
  peso = peso * 0.38
  print(peso, "Kg")
elif planeta ==2:
  peso = peso * 0.91
  print(peso, "Kg")
elif planeta ==3:
  peso = peso * 0.38
  print(peso, "Kg")
elif planeta ==4:
  peso = peso * 2.53
  print(peso, "Kg")
elif planeta ==5:
  peso = peso * 1.07
  print(peso, "Kg")
elif planeta ==6:
  peso = peso * 0.89
  print(peso, "Kg")
elif planeta ==7:
  peso = peso * 1.14
  print(peso, "Kg")
else:
  print("Invalid planet number")