infraccionMes = float(input("Introduce las infracciones: "))

porcenMatutino = 0.2
porcenVespertino = 0.35
porcenNocturno = 0.45

infraccionMatu = infraccionMes * porcenMatutino
infraccionVesper = infraccionMes * porcenVespertino
infraccionNoc = infraccionMes * porcenNocturno

diasMes = 30

if porcenMatutino != 0:
  promMatutino = infraccionMatu/(diasMes * porcenMatutino)
  print("Promedio diario matutino de infracciones:", promMatutino)
else:
  print("No se puede calcular el promedio diario matutino de infracciones, el porcentaje es cero")

if porcenVespertino != 0:
  promVespertino = infraccionVesper/(diasMes * porcenVespertino)
  print("Promedio diario vespertino de infracciones:", promVespertino)
else:
  print("No se puede calcular el promedio diario vespertino de infracciones, el porcentaje es cero")

if porcenNocturno != 0:
  promNocturno = infraccionNoc/(diasMes * porcenNocturno)
  print("Promedio diario nocturno de infracciones:", promNocturno)
else:
  print("No se puede calcular el promedio diario nocturno de infracciones, el porcentaje es cero")

print("FIN DEL PROGRAMA")