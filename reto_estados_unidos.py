#EJERCICIO 1:

import sys
from datetime import datetime

#A.: crea una lista que contenga un diccionario por cada estado. Cada elemento de la lista será un diccionario. 

estados = ["Alabama", "Florida", "Georgia", "South Carolina"]
poblacion_2000 = [4447100, 15982378, 8186453, 4012012]
poblacion_2001 = [4451493, 17054000, 8229823, 4023438]
residentes_2000 = [3870598, 13237167, 7440877, 3535770]
residentes_2001 = [3880476, 13548077, 7582146, 3567172]
muertes_2000 = [10622, 38103, 14804, 8581]
muertes_2001 = [15912, 166069, 15000, 9500]
latitudes = [33.258882, 27.756767, 32.329381, 33.687439]
longitudes = [-86.829534, -81.463983, -83.113737, -80.436374]
fechas_fundacion = ["14-12-1819", "03-03-1845", "12-02-1733", "26-03-1776"]

datos_estados = []

for estado, pop_2000, pop_2001, res_2000, res_2001, muertes_2000, muertes_2001, lat, lon, fecha in zip(
    estados, poblacion_2000, poblacion_2001, residentes_2000, residentes_2001, muertes_2000, muertes_2001, latitudes, longitudes, fechas_fundacion
):
    datos_estados.append({
        "estado": estado,
        "poblacion_2000": pop_2000,
        "poblacion_2001": pop_2001,
        "resid_menor_65_2000": res_2000,
        "resid_menor_65_2001": res_2001,
        "muertes_2000": muertes_2000,
        "muertes_2001": muertes_2001,
        "latitud": lat,
        "longitud": lon,
        "fecha_fundacion": fecha
    })


"""
D:
Incluid una nueva clave “Días desde fundación
nombre_estado” que sea el número de días que han pasado desde la fundación del
Estado hasta la actualidad. 
"""

def calcular_dias_desde_fundacion():
    hoy = datetime.today()                                  # obtener fecha actual

    for estado in datos_estados:
        date_str = estado['fecha_fundacion']
        format_str = "%d-%m-%Y"                             # cadena con formato "dd-mm-aaaa"
        fundacion = datetime.strptime(date_str, format_str) # convertir fecha con formato "dd-mm-aaaa" a objeto datetime
        dias = hoy - fundacion                              # calcular el delta (diferencía de días)
        estado['dias_desde_fundacion'] = dias.days          # guadar los días transcurridos en un nuevo campo 

def corregir_poblacion_florida():
    # Agregar un nuevo valor al diccionario
    for estado in datos_estados:                 
        if estado['estado'] == 'Florida':        # Identificamos clave Estado == Florida, si cumple la funcion, se accede a clave Poblacion 2001
          estado['poblacion_2001'] = 16054328    # se ingresa a la clave Población 2001 y colocamos el nuevo valor 
          break

def estado_antiguo_moderno():
    mas_dias = 0
    menos_dias = sys.maxsize

    for estado in datos_estados:
        dias = estado['dias_desde_fundacion']
        if dias > mas_dias:     # buscar el estado con más días desde su fundación
            mas_dias = dias
            mas_antiguo = estado
        if dias < menos_dias:   # buscar el estado con ménos días desde su fundación
            menos_dias = dias
            mas_moderno = estado

    años_antiguo = mas_dias // 365      
    años_moderno = menos_dias // 365      
    años_diferencia = años_antiguo - años_moderno    

    print('El estado más antiguo es',mas_antiguo['estado'],'con',años_antiguo,'años desde su fundación')
    print('El estado más moderno es',mas_moderno['estado'],'con',años_moderno,'años desde su fundación')
    print('La diferencia en años entre el estado más antiguo y el más moderno es de',años_diferencia,'años')
    

def listar_estados():
    # Imprimir la lista de diccionarios
    for estado in datos_estados:
        print(estado)   


calcular_dias_desde_fundacion()
corregir_poblacion_florida()
estado_antiguo_moderno()
#listar_estados()


