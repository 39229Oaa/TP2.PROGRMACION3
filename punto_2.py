#punto 2
conexiones=[("U001",(31.05, -118.24), "Activo"),("U002",(40.71,-74.00),"Inactivo")]
for usuario, (latitud, longitud),estado in conexiones:
    if estado=="Activo":
        print("El usuario", usuario, "esta", estado, "en las cordenadas", latitud, ",",longitud)
my_list_conexiones =list(conexiones)
print(type(my_list_conexiones))
my_list_conexiones.extend(["modifo la tupla"])
print(my_list_conexiones)
my_tuple_conexiones=tuple(my_list_conexiones)
print(type(my_tuple_conexiones))