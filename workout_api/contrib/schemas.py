from typing import Annotated
from pydantic import UUID4, BaseModel, Field
from datetime import datetime

class BaseSchema(BaseModel):
    class config:
        extra = "forbid"
        from_attributes = True

class OutMixin(BaseSchema):
    id: Annotated[UUID4, Field(Annotated="Identificador")]
    created_at: Annotated[datetime, Field(Annotated="Data de criação")]