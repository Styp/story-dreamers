from pydantic import BaseModel


class Payload(BaseModel):
    prompt: str