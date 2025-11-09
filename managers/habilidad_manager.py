import psycopg

from modelos import habilidad_model


class manager_habilidad:
     def agregar_habilidad (self, Habilidad:habilidad_model, cursor:psycopg.Cursor):
       
       cursor.execute("INSERT INTO habilidad (habilidad) VALUES=(%s)", (Habilidad.habilidad))

       return ("!!habilidad agregada!!")  