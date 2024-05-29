#-------------------------------------------------------------------
#
#                            EJERCICIO 2
#
#-------------------------------------------------------------------

import mysql.connector as myconector;
import json

conect= myconector.connect(user='root', password ='', host = 'localhost', database = 'estados_unidos', port = "3306")
query = conect.cursor()

query.execute("SELECT * FROM estados")
estados = query.fetchall()
print('\nEstados')
for estado in estados:
    print(estado)

query.execute("SELECT * FROM poblacion")
poblacion = query.fetchall()
print('\nPoblación')
for pop in poblacion:
    print(pop)

query.execute("SELECT * FROM muertes")
muertes = query.fetchall()
print('\nMuertes')
for muerte in muertes:
    print(muerte)

query.execute("SELECT * FROM residentes_65")
residentes = query.fetchall()
print('\nResidentes < 65')
for residente in residentes:
    print(residente)

query.close()

json_estados = json.dumps(estados)
json_poblacion = json.dumps(poblacion)
json_muertes = json.dumps(muertes)
json_residentes = json.dumps(residentes)

print('\nJSON Estados')
print(json_estados)

print('\nJSON Población')
print(json_poblacion)

print('\nJSON Muertes')
print(json_muertes)

print('\nJSON Residentes < 65')
print(json_residentes)