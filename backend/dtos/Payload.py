from pydantic import BaseModel


class PromptPayload(BaseModel):
    prompt: str


class TextPayload(BaseModel):
    text: str