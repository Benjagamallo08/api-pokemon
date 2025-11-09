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

@router.get ("/ver_habilidad")

def habilidad_get ( cursor: psycopg.Cursor = Depends (getCursor)):
    return habilidad_manager.ver_habilidad (cursor)

@router.delete ("/eliminar_pokemon/{id}")

def habilidad_delete ( id:int, cursor: psycopg.Cursor = Depends (getCursor)):
    return habilidad_manager.eliminar_habilidad (id, cursor)


@router.put ("/actualizar_habilidad/{id}")

def habilidad_put (id:int, nueva_habiliad:habilidad_model, cursor:psycopg.Cursor = Depends (getCursor)):
    return habilidad_manager.actualizar_habilidad (id, nueva_habiliad, cursor)


