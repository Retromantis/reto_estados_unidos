#-------------------------------------------------------------------
#
#                            EJERCICIO 2
#
#-------------------------------------------------------------------

import mysql.connector as myconector;

conect= myconector.connect(user='root', password ='', host = 'localhost', database = 'estados_unidos', port = "3306")
query = conect.cursor()

sentence = """

INSERT INTO estados (Id_Estado, Nombre, Fecha_Fundacion, Latitud, Longitud) VALUES 
   
  (1,"Alabama","14-12-1819","33.258.882", "-86.829.534"),
  (2,"Florida"," 03-03-1845 ","27.756.767 ", "-81.463.983"),
  (3,"Georgia"," 12-02-1733","32.329.381 ", "-83.113.737"),
  (4,"South Carolina"," 26-03-1776","33.687.439", "-80.436.374");


"""

sentence = """

INSERT INTO muertes (Id_Muertes, Id_Estado, Anio, Cantidad) VALUES
    (1, 1, 2000, 10622),
	(2, 1, 2001, 15912),
    (3, 2, 2000, 38103),
	(4, 2, 2001, 166069),
    (5, 3, 2000, 14804),
    (6, 3, 2001, 15000),
    (7, 4, 2000, 8581),
    (8, 4, 2001, 9500);
"""

sentence = """
INSERT INTO poblacion (Id_Poblacion, Id_Estado, Anio, Cantidad) VALUES
    (1, 1, 2000, 4447100),
	(2, 1, 2001, 4451493),
    (3, 2, 2000, 15982378),
	(4, 2, 2001, 17054000),
    (5, 3, 2000, 8186453),
    (6, 3, 2001, 8229823),
    (7, 4, 2000, 4012012),
    (8, 4, 2001, 4023438);

"""
sentence = """ INSERT INTO residentes_65 (Id_Residentes, Id_Estado, Anio, Cantidad) VALUES
        (1, 1, 2000, 3870598),
		(2, 2, 2001, 3880476),
		(3, 2, 2000, 13237167),
		(4, 2, 2001, 13548077),
		(5, 3, 2000, 7440877),
		(6, 3, 2001, 7582146),
		(7, 4, 2000, 3535770),
		(8, 4, 2001, 3567172);
"""

query.execute(sentence)


