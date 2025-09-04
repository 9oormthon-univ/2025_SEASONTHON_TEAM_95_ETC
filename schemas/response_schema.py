from pydantic import BaseModel

class ResultResponse(BaseModel):
    status: str
    results: dict