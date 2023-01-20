from pydantic import BaseModel, validator, constr


class AddCityModel(BaseModel):
    name: constr(max_length=64)

    @validator('name')
    def check_name(name):
        # check if this name exist on ow
        return name
