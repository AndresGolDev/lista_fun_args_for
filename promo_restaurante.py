"""
Sistema de Promociones en un Restaurante (*args)
Descripción
Eres el desarrollador de un sistema para un restaurante que ofrece descuentos en
productos seleccionados. Debes crear una función que reciba una lista de precios y calcule
el total a pagar, aplicando un descuento del 10% en los productos que superen los $100.
Requisitos
• La función se llamará lista_todo = lista_100 + producto.
• Debe recibir cualquier cantidad de precios de productos.
• Aplicar un 10% de descuento solo a los productos cuyo precio sea mayor a $100.
• Retornar el total a pagar después de aplicar los descuentos.

Ejemplo de uso:
total = calcular_total(50, 150, 200, 80, 120)
print(total) # Debe aplicar descuento a 150, 200 y 120
"""

def calcular_total(*precios):
    precios_list = list(precios)

    lista_100 = []
    lista_99 = []

    for precio in precios_list:
        if precio >= 100:
            lista_100.append(precio)
        else:
            lista_99.append(precio)

    suma_100 = sum(lista_100)
    suma_99 = sum(lista_99)
    porcentaje = suma_100 * 10 / 100

    lista_final = lista_100 + lista_99

    for lista in lista_final:
        if lista >= 100:
            return print(f"la suma de los productos con descuento es"
                         f" {sum(lista_final) - porcentaje}")

    return print(f"El total de productos sin descuentos es:"
                     f" {suma_99} ")

calcular_total(10,100)
