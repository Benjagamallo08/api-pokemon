from pydantic import BaseModel


class tipo_model (BaseModel):
    tipo: str
 



class pokemon_model(BaseModel):
    nombre:str

class  habilidad_model (BaseModel):
    habilidad:str


class pokedex_model (BaseModel):
    pokemon_id: int
    tipo_id:int
    habilidad_id:int









