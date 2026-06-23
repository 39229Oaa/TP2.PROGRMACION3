acceso_bd_clientes={"E01", "E03", "E05","E09"}
acceso_bd_finanzas={"E01", "E03","E08","E09"}
empleados_suspendidos={"E09","E10"}
doble_acceso=acceso_bd_clientes & acceso_bd_finanzas # devuelve los elementos que se encuentran en ambos conjuntos
print("Acceso doble")
print(doble_acceso)
acceso_exclusivo=acceso_bd_clientes ^ acceso_bd_finanzas #devuelve los elemento que no se repiten en ambos conjuntos
print ("Acceso exclusivo")
print(acceso_exclusivo)
acceso_totales= acceso_bd_clientes | acceso_bd_finanzas #junta todos lo elemento sin repetir
print ("acceso totales")
print(acceso_totales)
alerta_segurirdad=acceso_totales &empleados_suspendidos
print("alerta de seguridad")
print(alerta_segurirdad)

hola= "hola"
mundo = "mundo"
esto=hola-mundo
print(esto)
