# El sombrero seleccionador 

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

pregunta1 = int(input("¿Que prefieres: (1)Perros o (2)Gatos?"))

if pregunta1 == 1:
  Gryffindor = Gryffindor + 1
  Ravenclaw = Ravenclaw + 1
elif pregunta1 == 2:
  Hufflepuff = Hufflepuff + 1
  Slytherin = Slytherin + 1
else:
  print("Respuesta erronea.")

pregunta2 = int(input("¿Cuándo esté muerto, quiero que la gente me recuerde como: (1)Bueno, (2)Grande, (3)Sabio o (4)Audaz,?"))

if pregunta2 == 4:
  Gryffindor = Gryffindor + 2
elif pregunta2 == 1:
  Hufflepuff = Hufflepuff + 2
if pregunta2 == 2:
  Slytherin = Slytherin + 2
elif pregunta2 == 3:
  Ravenclaw = Ravenclaw + 2
else:
  print("Respuesta erronea.")

pregunta3 = int(input("¿Qué tipo de instrumento te gustaria aprender: (1)Violín, (2)Trompeta, (3)Piano o (4)Batería,?"))

if pregunta3 == 4:
  Gryffindor = Gryffindor + 4
elif pregunta3 == 1:
  Slytherin = Slytherin + 4
if pregunta2 == 2:
  Hufflepuff = Hufflepuff + 4
elif pregunta2 == 3:
  Ravenclaw = Ravenclaw + 4
else:
  print("Respuesta erronea.")


if Gryffindor >= Ravenclaw and Gryffindor >= Hufflepuff and Gryffindor >= Slytherin:
  print('🦁 Gryffindor!')
elif Ravenclaw >= Hufflepuff and Ravenclaw >= Slytherin:
  print('🦅 Ravenclaw!')
elif Hufflepuff >= Slytherin:
  print('🦡 Hufflepuff!')
else:
  print('🐍 Slytherin!')