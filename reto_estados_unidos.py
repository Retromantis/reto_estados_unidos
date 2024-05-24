#EJERCICIO 1:

import sys
from random import random
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

def buscar_estado(nombre):
    diccionario = {}
    nombre = nombre.lower()
    for estado in datos_estados:
        if estado['estado'].lower() == nombre:
            diccionario = estado
            break
    return diccionario


# busca en la lista un estado y devuelve un nuevo diccionario
def genenar_diccionario_estado(nombre):
    diccionario = {}
    estado = buscar_estado(nombre)
    if estado:
        for key in estado.keys():
            diccionario[key + '_' + nombre] = estado[key]
    return diccionario

    
def calcular_dias_desde_fundacion():
    for estado in datos_estados:
        date_str = estado['fecha_fundacion']
        format_str = "%d-%m-%Y"                             # cadena con formato "dd-mm-aaaa"
        fundacion = datetime.strptime(date_str, format_str) # convertir fecha con formato "dd-mm-aaaa" a objeto datetime
        dias = datetime.today() - fundacion                              # calcular el delta (diferencía de días)
        estado['dias_desde_fundacion'] = dias.days          # guadar los días transcurridos en un nuevo campo 


def corregir_poblacion_florida():
    # Agregar un nuevo valor al diccionario
    estado = buscar_estado('Florida')
    if estado:                 
        estado['poblacion_2001'] = 16054328    # se ingresa a la clave Población 2001 y colocamos el nuevo valor 


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

def porcentaje_mayores_65():
    #Realizamos para los mayores de 65 años en el 2000
    for estado in datos_estados:
        res_menor = estado['resid_menor_65_2000']
        total_pob = estado['poblacion_2000']

        porcentaje_mayor = ((total_pob - res_menor)/total_pob)*100
        porcentaje_mayor = round(porcentaje_mayor, 2)
        
        estado['porcentaje_mayor_65_años_2000'] = porcentaje_mayor


    #Luego, realizamos para los mayores de 65 años en el 2001

    for estado in datos_estados:
        res_menor = estado['resid_menor_65_2001']
        total_pob = estado['poblacion_2001']

        porcentaje_mayor = ((total_pob - res_menor)/total_pob)*100
        porcentaje_mayor = round(porcentaje_mayor, 2)
        
        estado['porcentaje_mayor_65_años_2001'] = porcentaje_mayor


def calcular_crecimiento_poblacion():
    alabama = genenar_diccionario_estado('Alabama')
    south_carolina = genenar_diccionario_estado('South Carolina')
    ratio_1 = random()
    ratio_2 = random()
    alabama['ratio_crecimiento'] = min(ratio_1,ratio_2)
    south_carolina['ratio_crecimiento'] = max(ratio_1,ratio_2)

    print(alabama)
    print(south_carolina)
    # TODO 


#Ejercicio 3: Solución desarrollada por María Tapia

#Creamos la funcion:
def proyeccion_poblacion_demografia(año_1, año_2):

    #Hacemos una nueva lista e iteramos solo los datos que necesitaremos: estados, poblacion 2000, 2001 y fecha fundacion:
    info_estados = []

    for estado, pobl_1, pobl_2, fund  in zip(estados, poblacion_2000, poblacion_2001, fechas_fundacion):
        info_estados.append({
            'estado': estado,
            'poblacion_2000': pobl_1,
            'poblacion_2001': pobl_2,
            'fecha_fundacion': fund
        })

    for estado in info_estados:
        pobl_1 = estado['poblacion_' + str(año_1)]    #Obtenemos las claves donde el año_1 ingresado es convertido en string para que pueda agregarse al texto y ser ubicado
        pobl_2 = estado['poblacion_' + str(año_2)]    #Igual con el año_2
        
        # Proyección de la población para el año siguiente al año_2
        ratio = pobl_2 / pobl_1
        proximo_año = año_2 + 1
        poblacion_proyectada = ratio * pobl_2
        
        # Calculamos t desde la fundación hasta 1900
        ''' Obtenemos el año de fundacion haciendo un .split que separara la fecha por cada "-" 
        que encontremos (ejemplo: "14-12-1819" lo pasa a: "14" "12" "1819") y con el [-1] selecciona 
        al ultimo elemento, en este caso el año'''  
        año_fundacion = int(estado['fecha_fundacion'].split("-")[-1])   
        t = 1900 - año_fundacion
        
        # Función demográfica P(t)
        P_t = (14500 * t + 7000) / (2 * t + 1)
        
        # Añadimos resultados al diccionario del estado
        estado['poblacion_' + str(proximo_año)] = poblacion_proyectada
        estado['poblacion_demografica'] = P_t

    for estado in info_estados:
        print(estado)        


calcular_dias_desde_fundacion()
corregir_poblacion_florida()
porcentaje_mayores_65()
#estado_antiguo_moderno()
#listar_estados()
#print(genenar_diccionario_estado('alabama'))
#calcular_crecimiento_ploblacion()

proyeccion_poblacion_demografia(2000, 2001)