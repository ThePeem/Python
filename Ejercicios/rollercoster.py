# Podras montarte en la atraccion?

altura = int(input("¿Cuánto mides?"))
dinero = int(input("¿Cuánto dinero tienes?"))

if altura >= 137 and dinero >= 10:
  print("Disfruta de la atracción!!")
elif altura < 137 and dinero >= 10:
  print("No eres lo suficientemente alto.")
elif altura >= 137 and dinero < 10:
  print ("No tienes suficiente dinero.")
else:
  print("No cumples ningun requisito.")