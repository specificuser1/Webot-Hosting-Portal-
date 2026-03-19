from pydantic import BaseModel

class TokenInput(BaseModel):
    token: str

class BulkTokens(BaseModel):
    tokens: list[str]

class StatusModel(BaseModel):
    activity: str
    text: str
