import psycopg

from modelos import pokedex_model


class manager_pokedex:

    def agregar_pokedex (self, pokedex:pokedex_model, cursor: psycopg.Cursor):

        cursor.execute ("INSERT INTO pokedex (pokemon_id,tipo_id,habilidad_id) VALUES (%s,%s,%s)", (pokedex.pokemon_id, pokedex.tipo_id, pokedex.habilidad_id))

        return "!!dato agregado a la pokedex!!"

    def ver_pokedex (self, cursor:psycopg.Cursor):
        res = cursor.execute( "SELECT pokemon.nombre, tipo.tipo, habilidad.habilidad FROM pokedex INNER JOIN pokemon ON pokedex.pokemon_id = pokemon.id_pokemon INNER JOIN tipo ON pokedex.tipo_id = tipo.id_tipo INNER JOIN habilidad ON pokedex.habilidad_id = habilidad.id_habilidad").fetchall()
        return [ {"nombre": row[0], "tipo": row[1], "habilidad": row[2] , } for row in res]
