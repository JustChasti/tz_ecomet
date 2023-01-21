from pydantic import BaseModel, validator, constr


class CityModel(BaseModel):
    name: constr(max_length=64)
