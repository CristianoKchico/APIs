from typing import Annotated, Optional
from pydantic import Field, PositiveFloat

from workout_api.categorias.schemas import CategoriaIn
from workout_api.centro_treinamento.schemas import CentroTreinamentoAtleta
from workout_api.contrib.schemas import BaseSchema, OutMixin

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description="nome do atleta", example="João", max_length=50)]
    cpf: Annotated[str, Field(description="cpf do atleta", example="12345678900", max_length=11)]
    idade: Annotated[int, Field(description="idade do atleta", example="30")]
    peso: Annotated[PositiveFloat, Field(description="peso do atleta", example="56.5")]
    altura: Annotated[PositiveFloat, Field(description="altura do atleta", example="1.75")]
    sexo: Annotated[str, Field(description="sexo do atleta", example="M", max_length=1)]
    categoria: Annotated[CategoriaIn, Field(description="categoria do atleta")]
    centro_treinamento: Annotated[CentroTreinamentoAtleta, Field(description="centro de treinamento do atleta")]

class AtletaIn(Atleta):
    pass

class AtletaOut(Atleta, OutMixin):
    pass

class AtletaUpdate(BaseSchema):
    nome: Annotated[Optional[str], Field(None, description="nome do atleta", example="João", max_length=50)]
    idade: Annotated[Optional[int], Field(None, description="idade do atleta", example="30")]