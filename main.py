from fastapi import FastAPI
from  routes.router1 import router as RouterTipo
from routes.router_pokemon import router as RouterPokemon



app= FastAPI()
app.include_router(RouterTipo)
app.include_router(RouterPokemon)


