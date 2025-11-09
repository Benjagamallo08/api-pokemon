import psycopg

from modelos import pokemon_model


class pokemon_manager:
    def agregar_pokemon (self, pokemon:pokemon_model, cursor:psycopg.Cursor):

        cursor.execute ("INSERT INTO pokemon (nombre) VALUES (%s)", (pokemon.nombre,))
        return "!!!pokemon agregado !!!"
    
    def ver_pokemon (self, cursor: psycopg.Cursor):

        res= cursor.execute ("SELECT nombre,id_pokemon FROM pokemon").fetchall()

        return [{"id": row [1] , "nombre": row [0]} for row in res]
    
    def eliminar_pokemon (self,id:int, cursor: psycopg.Cursor):
        cursor.execute ( "DELETE FROM pokemon WHERE id_pokemon=%s", (id,))

        return "pokemon eliminado"
    
    def actualizar_pokemon (self, id: int, nuevo_pokemon: pokemon_model, cursor:psycopg.Cursor):
        cursor.execute ("UPDATE  pokemon SET nombre= %s WHERE id_pokemon=%s", (nuevo_pokemon.nombre,id,))
        return "pokemon actualizado"
