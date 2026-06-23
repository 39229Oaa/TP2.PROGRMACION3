#punto 3
ventas_hoy = ["TEC","HOG","TEC","JUG","TEC", "HOG","SUD"]
frecuencia_ventas={}
for categoria in ventas_hoy:
    frecuencia_ventas[categoria] = frecuencia_ventas.get(categoria,0)+1
    print("frecuencia de ventas")
    print(frecuencia_ventas)
categoria_unica = (frecuencia_ventas.keys())
print("\Categoria Unica:")
print(categoria_unica)

