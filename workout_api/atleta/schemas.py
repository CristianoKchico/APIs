from typing import Annotated
from pydantic import Field, PositiveFloat

from workout_api.contrib.schemas import BaseSchema, OutMixin

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description="nome do atleta", example="João", max_length=50)]
    cpf: Annotated[str, Field(description="cpf do atleta", example="12345678900", max_length=11)]
    idade: Annotated[int, Field(description="idade do atleta", example="30")]
    peso: Annotated[PositiveFloat, Field(description="peso do atleta", example="56.5")]
    altura: Annotated[PositiveFloat, Field(description="altura do atleta", example="1.75")]
    sexo: Annotated[str, Field(description="sexo do atleta", example="M", max_length=1)]

class AtletaIn(Atleta):
    pass

class AtletaOut(Atleta, OutMixin):
    pass
