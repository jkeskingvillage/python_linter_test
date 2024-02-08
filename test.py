from datetime import datetime
from pydantic import BaseModel, NoneStr


class Model(BaseModel):
    age: int
    first_name = "John"
    last_name: NoneStr = None
    signup_ts: datetime | None = None
    list_of_ints: list[int]


m = Model(age=42, list_of_ints=[1, "2", b"3"])
print(m.middle_name)  # not a model field!
Model()  # will raise a validation error for age and list_of_ints
