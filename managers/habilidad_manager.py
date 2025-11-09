import psycopg

from modelos import habilidad_model


class manager_habilidad:
     def agregar_habilidad (self, Habilidad:habilidad_model, cursor:psycopg.Cursor):
       
       cursor.execute("INSERT INTO habilidad (habilidad) VALUES (%s)", (Habilidad.habilidad,),)

       return ("!!habilidad agregada!!")  
     
     def ver_habilidad ( self, cursor:psycopg.Cursor):
         res = cursor.execute ( "SELECT id_habilidad, habilidad FROM habilidad").fetchall ()
         return [{"id": row [0], "habilidad":  row[1]} for row in res]
         