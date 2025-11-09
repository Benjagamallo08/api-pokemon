from fastapi import FastAPI
from  routes.router1 import router as RouterTipo
from routes.router_pokemon import router as RouterPokemon
from routes.router_habilidad import router as RouterHablidad



app= FastAPI()
app.include_router(RouterTipo)
app.include_router(RouterPokemon)
app.include_router(RouterHablidad)


