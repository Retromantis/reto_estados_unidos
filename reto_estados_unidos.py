import sys
import folium
import numpy as np
import random 
from datetime import datetime


# Ejercicio 1.a: Solución desarrollada por María Tapia

# crea una lista que contenga un diccionario por cada estado. Cada elemento de la lista será un diccionario
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

for estado in datos_estados:
    print(estado)

# Agregar un nuevo valor al diccionario
for estado in datos_estados:                 
   if estado['estado'] == 'Florida':         # Identificamos clave Estado == Florida, si cumple la funcion, se accede a clave Poblacion 2001
      estado['poblacion_2001'] = 16054328    # se ingresa a la clave Población 2001 y colocamos el nuevo valor 
      break

      
# Ejercicio 1.b: Solución desarrollada por Victor Zegarra

# generar tantos diccionarios como Estados tengamos con el formato "llave_nombre_estado"
def genenar_diccionarios_estados():
    for estado in datos_estados:
        diccionario = {}
        nombre = estado['estado']
        for key in estado.keys():
            diccionario[key + '_' + nombre] = estado[key]
        print(diccionario)
    print()


# Ejercicio 1.c: Solución desarrollada por María Tapia

# correción de la población del estado de Florida
def corregir_poblacion_florida():
    for estado in datos_estados:
        if estado['estado'] == 'Florida':
            # Agregar un nuevo valor al diccionario
            estado['poblacion_2001'] = 16054328    # se ingresa a la clave Población 2001 y colocamos el nuevo valor
            break


# Ejercicio 1.d: Solución desarrollada por Victor Zegarra y Rafael

# calcular los días desde su fundación de los estados    
def calcular_dias_desde_fundacion():
    for estado in datos_estados:
        date_str = estado['fecha_fundacion']
        format_str = "%d-%m-%Y"                             # cadena con formato "dd-mm-aaaa"
        fundacion = datetime.strptime(date_str, format_str) # convertir fecha con formato "dd-mm-aaaa" a objeto datetime
        dias = datetime.today() - fundacion                              # calcular el delta (diferencía de días)
        estado['dias_desde_fundacion'] = dias.days          # guadar los días transcurridos en un nuevo campo 


# Ejercicio 1.e: Solución desarrollada por Rafael

# calcular el porcentaje de personas mayores de 65 años en cada estado 
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


# Ejercicio 1.f: Solución desarrollada por Victor Zegarra

# mostrar el estado más antiguo y el más moderno, y la difencia de años entre ellos
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

    print('El estado más antiguo es ',mas_antiguo['estado'],'con',años_antiguo,'años desde su fundación')
    print('El estado más moderno es ',mas_moderno['estado'],'con',años_moderno,'años desde su fundación')
    print('La diferencia en años entre el estado más antiguo y el más moderno es de',años_diferencia,'años\n')

def listar_estados():
    # Imprimir la lista de diccionarios
    for estado in datos_estados:
        print(estado,'\n')   


# Ejercicio 2: Solución desarrollada por Rafael

def calcular_crecimiento_poblacion():
    pob_alabama = 0
    pob_s_carolina = 0

    # Sacamos los valores de las poblaciones de los estados solicitados del 2001

    for estado in datos_estados:
        if(estado['estado'] == 'Alabama'):
            pob_alabama = estado['poblacion_2001']
        elif (estado['estado'] == 'South Carolina'):
            pob_s_carolina = estado['poblacion_2001']

    ratio_menor = 0
    ratio_mayor = 0.1

    año_pob = 2022

    #Generamos las tasa de crecimiento aleatorias

    tasa_crecimiento_alabama = random.uniform(ratio_menor, ratio_mayor)
    tasa_crecimiento_south_carolina = random.uniform(tasa_crecimiento_alabama, ratio_mayor)

    #Para las preguntas 1 y 2 se realizará lo siguiente

    while (pob_s_carolina <= pob_alabama):

        #Calcular nuevas poblaciones de cada año

        n_pob_alabama = pob_alabama*(1 + tasa_crecimiento_alabama)
        n_pob_south_carolina = pob_s_carolina*(1 + tasa_crecimiento_south_carolina)

        pob_alabama = n_pob_alabama
        pob_s_carolina = n_pob_south_carolina

        año_pob += 1

    print(f"Años que tardará en alcanzar a la población {año_pob - 2001}")
    print(f"Carolina del Sur alcanzará a Alabama en el año {año_pob}")

    #Para la pregunta 3 se aplicará la tasa de fallecidos

    fall_alabama = 0
    fall_s_carolina = 0

    for estado in datos_estados:
        if(estado['estado'] == 'Alabama'):
            fall_alabama = estado['muertes_2001']
        elif (estado['estado'] == 'South Carolina'):
            fall_s_carolina = estado['muertes_2001']

    t_f_alabama = fall_alabama / 4451493
    t_f_s_carolina = fall_s_carolina / 4023438


    while (pob_s_carolina <= pob_alabama):

        #Calcular nuevas poblaciones de cada año

        n_pob_alabama = pob_alabama*(1 + tasa_crecimiento_alabama - t_f_alabama)
        n_pob_south_carolina = pob_s_carolina*(1 + tasa_crecimiento_south_carolina - t_f_s_carolina)

        pob_alabama = n_pob_alabama
        pob_s_carolina = n_pob_south_carolina

        año_pob += 1

    print(f"Años que tardará en alcanzar a la población {año_pob - 2001}")
    print(f"Carolina del Sur alcanzará a Alabama en el año {año_pob}\n")


# Ejercicio 3: Solución desarrollada por María Tapia

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

    print()    


# Ejercicio 3: Solución desarrollada por Patricio

#Instrucciones reto 1.3
#Cread una función que genere una proyección para el año 2002, utilizando como ratio
#la comparativa entre los años 2000 y 2001. De tal forma:
#Población Año 2002 = Población Año 2001 / Población Año 2000 x Población año 2001.
#Tras un estudio demográfico se ha determinado que el número de habitantes de cierta población, 
#en los próximos años, vendrá dado por la función: P(t) = 14500t + 7000/2t + 1 donde t son los años transcurridos entre
#la fundación del Estado y 1900.
#En la misma función, devolved la población que tendría cada Estado bajo la estimación que devuelve ese estudio demográfico.
#Añadid los resultados a cada diccionario de la lista.


# que hacer ? 
# 1) creo la funcion que genera proyeccion para el 2002

def func_ecu_pobla2002(poblacion_2000, poblacion_2001):
    return (poblacion_2001 / poblacion_2000) * poblacion_2001


# 2) creo la funcion para calcular poblacion usando ecuacion demografica P(t) = 14500t + 7000/2t + 1 (como tomamos la ecuacion ?)

def func_ecu_demografica(t):
    # AQUI HAY QUE DISCUTIR DE QUE MANERA LA TOMAMOS, los parentesis
    return 18000 * t + 1


# 2.2) (hacer t= año de fundacion - 1900), funcion p(t), resultado P(t) para cada estado


def func_edit_proyecydemo():
    for estado in datos_estados:
        # Proyección para el año 2002
        estado['poblacion_2002'] = func_ecu_pobla2002(estado['poblacion_2000'], estado['poblacion_2001'])
        
        # Calculo años desde la fundación hasta 1900
        fecha_fundacion = datetime.strptime(estado['fecha_fundacion'], "%d-%m-%Y")
        
        # AQUI HAY QUE REVISAR SI LA RESTA NO ES  AL REVÉS, MENCIONA LA DIFERENCIA PERO ESTO DEPENDE DE LA FECHA DE FUNDACION SI ES ANTERIOR O POSTERIOR
        t = 1900 - fecha_fundacion.year
        # (entendi de que debe ser para cada estado)
        
        # Población demográfica
        estado['poblacion_demografica'] = func_ecu_demografica(t)


# Ejercicio 4: Solución desarrollada por Mayra Guadalupe Arias Lopez

def generar_mapa_poblacion_2002(html_filename):
    # Crear un mapa centrado en la primera coordenada
    map_eua = folium.Map(location = [30.101271,-82.370146],zoom_start = 6)
    folium.Marker(location = [30.101271,-82.370146]).add_to(map_eua)

    #Coloca circulo en la posicion indicada
    folium.Circle(location = [30.101271,-82.370146],color = "red",fill_color = "red", radius = 20.02, weight = 40, fill_opacity = 0.5).add_to(map_eua)

    # Definir las listas de coordenadas como arrays
    y = np.array([-83.194062, -86.680734, -83.804601, -80.926614])
    x = np.array([32.67853, 32.576226, 27.59468, 33.605719])

    # Agregar circulos para cada coordenada
    for i in range(4):
        circle = folium.Circle((x[i], y[i]),color = "blue",fill_color = "red", radius = 20.02, weight = 40, fill_opacity = 0.5).add_to(map_eua)
    
    map_eua.save(html_filename)
    
    

genenar_diccionarios_estados()

corregir_poblacion_florida()
calcular_dias_desde_fundacion()
porcentaje_mayores_65()

estado_antiguo_moderno()
calcular_crecimiento_poblacion()

#llamado del ejercicio 3: Solucionado por María
proyeccion_poblacion_demografia(2000, 2001)

#llamado del ejercicio 3: Soluciónado por Patricio
func_edit_proyecydemo()

# 3) Muestra diccionarios y resultados finales
listar_estados()

#generar_mapa_poblacion_2002('../index.html')