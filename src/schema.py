from pydantic import BaseModel

# define uma classe que herda da BaseModel do Pydantic
# define um CONTRATO de DADOS / SCHEMA DE DADOS/ VIEW da API
# define como eu desejo que meus dados sejam
# o Pydantic faz VALIDAÇÃO e DESCERIALIZAÇÃO
class PokemonSchema(BaseModel):
    name: str
    type: str

    class Config:
        orm_mode = True