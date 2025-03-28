#CREA UN DICCIONARIO LLAMADO INFOEMACION PERSONAL
informacion_personal = {
    "NOMBRE": "Marylex Garcia",
    "EDAD": 29,
    "CIUDAD": "Quito",
    "PROFESION": "Paramedico"
}

#ACCEDEMOS AL VALOR  CLAVE DE CIUDAD
ciudad_actual = informacion_personal["CIUDAD"]
print(f"LA CIUDAD ACTUAL ES: {ciudad_actual}")

#MODIFICAMOS LA CIUDAD
informacion_personal["CIUDAD"] = "Cuenca"
ciudad_nueva = informacion_personal["CIUDAD"]
print(f"LA NUEVA CIUDAD ES: {ciudad_nueva}")

#AGREGO UNA  NUEVA OPCION QUE MUESTRE EL CARGO O PROFESION
informacion_personal["CARGO PROFESION"] = "Paramedioc Cruz Roja Ecuador "
print(f"La información actualizada es: {informacion_personal}")

#VERIFICAMOS SI EL DATO TELEFONO EXISTE Y COMO NO EXISTE AGREGO UN TELEFONO FICTICIO.
if "TELEFONO" not in informacion_personal:
    informacion_personal["TELEFONO"] = "987654321"
    print(f"SE AGREGO EL TELEFONONº: {informacion_personal['TELEFONO']}")

#ELIMAMOS EL DATO EDAD DEL DICCIONARIO
del informacion_personal["EDAD"]
print(f"LA INFORMACION ACTUALIZDA ES: {informacion_personal}")

#Imprime el diccionario resultante
print("EL RESULTADO DEL DICIONARIO ES :")
for informacion, datos in informacion_personal.items():
    print(f"{informacion}: {datos}")