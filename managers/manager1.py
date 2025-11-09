
from modelos import tipo_model

import psycopg


class tipo_manager:


    def agregar_tipo (self, Tipo: tipo_model, cursor: psycopg.Cursor):

        cursor.execute ( "INSERT INTO tipo (tipo) VALUES (%s)", ( Tipo.tipo,),)
        return "!!! Tipo agregado !!"
    
    def ver_tipo (self, cursor: psycopg.Cursor):

       res= cursor.execute ( "SELECT id_tipo, tipo FROM tipo").fetchall ()

       return [{"id": row [0], "tipo":  row[1]} for row in res]
    
    def actualizar_tipo (self,id: int, nuevo_tipo: tipo_model, cursor:psycopg.Cursor):
        cursor.execute ("UPDATE  tipo SET tipo= %s WHERE id_tipo=%s", (nuevo_tipo.tipo,id,))
        return "tipo actualizado"
    

    def eliminar_tipo (self,  id: int, cursor: psycopg.Cursor) :
        cursor.execute ( "DELETE FROM tipo WHERE id_tipo=%s", (id,))
        return "tipo eliminado"