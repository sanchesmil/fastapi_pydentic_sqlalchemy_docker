import requests 
from schema import PokemonSchema
from db import engine, SessionLocal, Base
from model import Pokemon

Base.metadata.create_all(bind=engine)

def fetch_pokemon_data(pokemon_id: int):
     #response = requests.get(url="https://www.fab.mil.br/")
    #URL = f"https://pokeapi.co/api/v2/pokemon/{id}"
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    if response.status_code == 200:
        data = response.json()
        types = ', '.join(type['type']['name'] for type in data['types'])
        return PokemonSchema(name=data['name'],type=types)
    else:
        return None

def add_pokemon_to_db(pokemon_schema: PokemonSchema) -> Pokemon:
    with SessionLocal() as db:
        db_pokemon = Pokemon(name=pokemon_schema.name, type=pokemon_schema.type)
        db.add(db_pokemon)
        db.commit()
        db.refresh(db_pokemon)
    return db_pokemon