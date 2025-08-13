from datetime import date
from pydantic import BaseModel,RootModel, Field, ConfigDict
from typing import Annotated
from tools.fakers import fake

class CreateTransactionSchema(BaseModel):

    model_config = ConfigDict(populate_by_name=True)
    
    description: Annotated[str, Field(default_factory=fake.sentence)]
    category: Annotated[str, Field(default_factory=fake.category)]
    debit: Annotated[float | str | None, Field(default_factory=fake.money)]
    credit: Annotated[float | str | None, Field(default_factory=fake.money)]
    transaction_date: Annotated[date, Field(alias='transactionDate', default_factory=fake.date)]

class UpdateTransactionSchema(BaseModel):

    model_config = ConfigDict(populate_by_name=True)

    description: Annotated[str | None, Field(default_factory=fake.sentence)]
    category: Annotated[str | None, Field(default_factory=fake.category)]
    debit: Annotated[float | str | None, Field(default_factory=fake.money)]
    credit: Annotated[float | str | None, Field(default_factory=fake.money)]
    transaction_date: Annotated[date | None, Field(alias='transactionDate', default_factory=fake.date)]

class OperationSchema(CreateTransactionSchema):

    id: int | str

class OperationsSchema(RootModel):

    root: list[OperationSchema]
