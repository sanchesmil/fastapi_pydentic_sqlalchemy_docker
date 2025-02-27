import requests
from pydantic import BaseModel

# define uma classe que herda da BaseModel do Pydantic
# define um CONTRATO de DADOS / SCHEMA DE DADOS/ VIEW da API
# define como eu desejo que meus dados sejam
# o Pydantic faz VALIDAÇÃO e DESCERIALIZAÇÃO
class PokemonSchema(BaseModel):
    name: str
    type: str

    class Config:
        from_attributes = True

def pegar_pokemon(id:int) -> PokemonSchema:
    #response = requests.get(url="https://www.fab.mil.br/")
    URL = f"https://pokeapi.co/api/v2/pokemon/{id}"
    response = requests.get(URL)
    data = response.json()
    data_types = data['types']
    types_list = []

    for type_info in data_types:
        types_list.append(type_info['type']['name'])

    types = ','.join(types_list)
    return PokemonSchema(name=data['name'],type=types)

if __name__ == "__main__":
    print(pegar_pokemon(10))
    print(pegar_pokemon(23))
    print(pegar_pokemon(17))

