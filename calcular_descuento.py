def calcular_descuento(monto_total, porcentaje_descuento):
    # Calcula el descuento aplicando el porcentaje al monto total
    descuento = (monto_total * porcentaje_descuento) / 100
    return  descuento
monto_total = 6000
porcentaje_descuento = 10
descuento_calculado = calcular_descuento(monto_total, porcentaje_descuento)

#Imprime  el monto total que en este caso es **6000**
print(f"EL MONTO TOTAL ES  :{monto_total}")
#Imprime  el monto del descuento  que en este caso es el 10%
print(f"EL MONTO DEL DESCUENTO ES : {descuento_calculado}")
