import psycopg

from modelos import habilidad_model


class manager_habilidad:
     def agregar_habilidad (self, Habilidad:habilidad_model, cursor:psycopg.Cursor):
       
       cursor.execute("INSERT INTO habilidad (habilidad) VALUES (%s)", (Habilidad.habilidad,),)

       return ("!!habilidad agregada!!")  
     
     def ver_habilidad ( self, cursor:psycopg.Cursor):
        res = cursor.execute ( "SELECT id_habilidad, habilidad FROM habilidad").fetchall ()
        return [{"id": row [0], "habilidad":  row[1]} for row in res]

     def eliminar_habilidad (self, id:int, cursor:psycopg.Cursor):

        cursor.execute ("DELETE FROM habilidad WHERE id_habilidad=%s", (id,))
        return "habilidad eliminada"
     
     def actualizar_habilidad (self,id:int, nueva_habilidad:habilidad_model, cursor:psycopg.Cursor):

        cursor.execute ("UPDATE habilidad SET habilidad=%s WHERE id_habilidad=%s", (nueva_habilidad.habilidad, id))
        return "Habilidad actualizada"