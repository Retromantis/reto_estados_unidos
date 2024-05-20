#EJERCICIO 1:
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

# 
datos_estados = []

for estado, pop_2000, pop_2001, res_2000, res_2001, muertes_2000, muertes_2001, lat, lon, fecha in zip(
    estados, poblacion_2000, poblacion_2001, residentes_2000, residentes_2001, muertes_2000, muertes_2001, latitudes, longitudes, fechas_fundacion
):
    datos_estados.append({
        "Estado": estado,
        "Población 2000": pop_2000,
        "Población 2001": pop_2001,
        "Residentes < 65 años 2000": res_2000,
        "Residentes < 65 años 2001": res_2001,
        "Muertes 2000": muertes_2000,
        "Muertes 2001": muertes_2001,
        "Latitud": lat,
        "Longitud": lon,
        "Fecha fundación": fecha
    })

# Imprimir la lista de diccionarios

for estado in datos_estados:
    print(estado)
