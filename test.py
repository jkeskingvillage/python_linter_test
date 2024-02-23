from datetime import datetime
from typing import Optional
from pydantic import BaseModel, NoneStr


class Model(BaseModel):
    age: int
    first_name = "John"
    last_name: NoneStr = None
    signup_ts: Optional[datetime] = None
    list_of_ints: list[int]


m = Model(age=42, list_of_ints=[1, "2", b"3"])
print(m.middle_name)  # not a model field!
Model()  # will raise a validation error for age and list_of_ints


def some_func(n):
    return n * n


def some_other_func(n: int):
    return n * n


def some_different_func(n: int) -> int:
    return n * n


def get_model(model: Model) -> None:
    return model.model_copy(deep=True)


def get_other_model(model: Model) -> Model:
    return model.model_copy(deep=True)
