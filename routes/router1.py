from fastapi import APIRouter , Depends
from managers.manager1 import tipo_manager
import psycopg
from modelos import tipo_model

from managers.conexion import getCursor

tipo= tipo_manager()

router= APIRouter (prefix= "/tipo" , tags= ["tipo routes"])

@router.post ( "/agregar_tipo")

def post_tipo( Tipo: tipo_model, cursor: psycopg.Cursor = Depends (getCursor) ):
    res=  tipo.agregar_tipo (Tipo, cursor)
    return res

@router.get ("/ver_tipos")

def get_tipo (cursor: psycopg.Cursor = Depends (getCursor)):

    res= tipo.ver_tipo (cursor)
    return res

@router.put ( "/actualizar_tipo/{id}")

def update_tipo ( id:int,nuevo_tipo:tipo_model, cursor: psycopg.Cursor =Depends(getCursor)):
    return tipo.actualizar_tipo (id, nuevo_tipo, cursor)

@router.delete ( "/eliminar_tipo/{id}")

def delete_tipo ( id:int, cursor: psycopg.Cursor = Depends (getCursor)):
    res= tipo.eliminar_tipo (id, cursor)

    return {res}
  




