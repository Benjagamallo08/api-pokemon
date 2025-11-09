from pydantic import BaseModel


class tipo_model (BaseModel):
    tipo: str
 



class pokemon_model(BaseModel):
    nombre:str

class  habilidad_model (BaseModel):
    habilidad:str








