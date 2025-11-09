import psycopg
from fastapi import APIRouter , Depends
from modelos import pokemon_model
from managers.pokemon_manager import pokemon_manager

from managers.conexion import getCursor

manager_pokemon= pokemon_manager ()


router = APIRouter (prefix= "/pokemon" , tags=["pokemon routes"])

@router.post ("/agregar_pokemon")

def pokemon_post (pokemon:pokemon_model, cursor:psycopg.Cursor = Depends(getCursor)):
    return manager_pokemon.agregar_pokemon (pokemon, cursor)

@router.get ("/ver_pokemon")

def pokemon_get (cursor:psycopg.Cursor = Depends (getCursor)):
    return manager_pokemon.ver_pokemon (cursor)

@router.delete ("/borrar_pokemon/{id}")

def pokemon_delete (id:int ,cursor: psycopg.Cursor = Depends (getCursor)):

    return manager_pokemon.eliminar_pokemon (id, cursor)


@router.put ("/actualizar_pokemon/{id}")

def pokemon_update ( id:int, nuevo_pokemon:pokemon_model, cursor: psycopg.Cursor =Depends(getCursor)):
    return manager_pokemon.actualizar_pokemon (id, nuevo_pokemon, cursor)




