import psycopg 
from modelos import pokedex_model
from fastapi import APIRouter, Depends
from managers.conexion import getCursor
from managers.pokedex_manager import manager_pokedex

pokedex_man= manager_pokedex ()


router = APIRouter (prefix="/pokedex" , tags=["pokedex routes"])

@router.post ("/agregar_a_la_pokedex")

def pokedex_post( pokedex:pokedex_model, cursor:psycopg.Cursor = Depends (getCursor)):
    return  pokedex_man.agregar_pokedex (pokedex, cursor)

@router.get ("/ver_pokedex")

def pokedex_get ( cursor: psycopg.Cursor = Depends (getCursor)):

     res = pokedex_man.ver_pokedex(cursor)
     return res





