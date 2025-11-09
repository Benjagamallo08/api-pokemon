from pydantic import BaseModel


class tipo_model (BaseModel):
    tipo: str
 



class pokemon_model(BaseModel):
    nombre:str

class  boletin_model (BaseModel):

    id_materia: int
    id_alumno: int





