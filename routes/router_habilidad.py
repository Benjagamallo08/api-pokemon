import psycopg
from fastapi import APIRouter , Depends
from managers.conexion import getCursor
from managers.habilidad_manager import manager_habilidad
from modelos import habilidad_model


habilidad_manager = manager_habilidad ()

router= APIRouter (prefix= "/habilidad" , tags= ["habilidad routes"])

@router.post ("/agegar_habilidad")
def habilidad_post (Habilidad: habilidad_model , cursor: psycopg.Cursor = Depends (getCursor)):
    return habilidad_manager.agregar_habilidad (Habilidad, cursor)

router.get ("/ver_habilidad")

def habilidad_get ( cursor: psycopg.Cursor = Depends (getCursor)):
    return habilidad_manager.ver_habilidad (cursor)




