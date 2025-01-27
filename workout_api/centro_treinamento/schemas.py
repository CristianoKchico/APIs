from typing import Annotated
from pydantic import Field, UUID4
from workout_api.contrib.schemas import BaseSchema


class CentroTreinamentoIn(BaseSchema):
    nome: Annotated[str, Field(description="nome do centro de treinamento", example="CT Wolves", max_length=20)]
    endereco: Annotated[str, Field(description="endereço do centro de treinamento", example="Via Global A, 30", max_length=60)]
    proprietario: Annotated[str, Field(description="proprietario do centro de treinamento", example="Chico", max_length=30)]


class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated[str, Field(description="Nome do centro de treinamento", example="CT Wolves", max_length=20)]


class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description="Identificador do centro de treinamento")]
