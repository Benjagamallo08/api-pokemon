import psycopg

from modelos import habilidad_model


class manager_habilidad:
    def agregar_habilidad (self, habilidad:habilidad_model, cursor:psycopg.Cursor):
       cursor.execute("INSERT INTO habilidad (habilidad) VALUES=(%s)", (habilidad.habilidad))

       return ("!!habilidad agregada!!")  